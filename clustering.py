from sentence_transformers import SentenceTransformer
from sklearn.cluster import AgglomerativeClustering
import numpy as np
import pandas as pd
from django.db import models
from helpers import preprocess_documents
from scipy.spatial.distance import euclidean

from typing import List


embedder = SentenceTransformer('all-MiniLM-L6-v2')

NUMBER_OF_CLUSTERS = 14


def cluster_paragraphs(paragraphs: List, flag):
    """
        Clusters paragraphs using the sentence transformer model and agglomerative clustering.
        input: list of paragraphs
        output: list of tuples (paragraph, cluster)
    """
    cleaned_paragraphs = preprocess_documents(paragraphs)
    embeddings = embedder.encode(cleaned_paragraphs)
    # Normalize the embeddings to unit length
    embeddings = embeddings /  np.linalg.norm(embeddings, axis=1, keepdims=True)

    # Perform kmean clustering
    clustering_model = AgglomerativeClustering(n_clusters=None, distance_threshold=2)
    clustering_model.fit(embeddings)
    cluster_assignment = clustering_model.labels_

    clusters = []

    for index, cluster in enumerate(cluster_assignment):
        clusters.append((index, cluster))
    
    # embeddings is called corpus_embeddings in the original code
    return clustering_model, embeddings, clusters

def get_data(flag):
    projects = []
    if flag == 'user':
        df = pd.DataFrame(list(models.Project.objects.all().values()))
        for i in range(len(df)):
            project = str(df['project_description'][i]) + \
                      str(df['keywords'][i])  + \
                      str(df['fields_of_science'][i]) +\
                      str(df['participation_tasks'][i])
            projects.append(project)
    else:
        df = pd.DataFrame(list(models.Contributer.objects.all().values()))
        for i in range(len(df)):
            project = str(df['description'][i]) + \
                      str(df['fields_of_science'][i])
            projects.append(project)

    return projects

def get_cluster(text: str, flag: str, number_of_clusters=NUMBER_OF_CLUSTERS):
    """
        Returns the cluster in which the text belongs to.
        input: text
        output: cluster number
    """

    # this is a quick and dirty "fix"

    # this should be a call to the database
    projects = get_data(flag)
    
    clustering_model, corpus_embeddings, clusters = cluster_paragraphs(projects, flag)


    text_embedding = embedder.encode(text)
    text_embedding = text_embedding / np.linalg.norm(text_embedding)

    # Calculate centroids of each cluster
    cluster_centers = []
    for cluster_label in np.unique(clustering_model.labels_):
        cluster_mask = (clustering_model.labels_ == cluster_label)
        cluster_center = np.mean(corpus_embeddings[cluster_mask], axis=0)
        cluster_centers.append(cluster_center)

    # Find the nearest cluster to the new paragraph
    nearest_cluster_index = min(range(len(cluster_centers)), key=lambda i: euclidean(text_embedding, cluster_centers[i]))

    return nearest_cluster_index

