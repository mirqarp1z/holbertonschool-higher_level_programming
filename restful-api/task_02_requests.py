#!/usr/bin/python3
"""
Task 2: Consuming and processing data from an API using Python.
"""

import requests
import csv


def fetch_and_print_posts():
    """Fetch posts from JSONPlaceholder and print status + titles."""
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    # If successful, parse and print titles
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """Fetch posts and save selected data into posts.csv."""
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        # Extract only id, title, and body into a list of dicts
        processed_posts = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            }
            for post in posts
        ]

        # Write to CSV
        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(processed_posts)
