provider "google" {
  project     = "gke-428821"
  region      = "us-central1"
}

resource "google_container_cluster" "primary" {
  name     = "mdsamshad-k8s-t"
  location = "us-central1-a"

  initial_node_count       = 1
  remove_default_node_pool = true
  deletion_protection      = false
}

resource "google_container_node_pool" "primary_preemptible_nodes" {
  name       = "mdsamshad-pool-1"
  cluster    = google_container_cluster.primary.id
  node_count = 1

  node_config {
    disk_size_gb = 20
    disk_type    = "pd-standard"

    preemptible  = true
    machine_type = "e2-small"
    image_type   = "COS_CONTAINERD"
  }
}