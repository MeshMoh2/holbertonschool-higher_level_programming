#!/usr/bin/python3
"""Module to consume API data using requests and process JSON into CSV."""

import requests
import csv


def fetch_and_print_posts():
    """
    Fetch all posts from JSONPlaceholder and print status code and titles.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get('title'))


def fetch_and_save_posts():
    """
    Fetch posts and save selected data (id, title, body) into posts.csv.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        data = [
            {'id': post['id'], 'title': post['title'], 'body': post['body']}
            for post in posts
        ]

        with open('posts.csv', mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(data)
