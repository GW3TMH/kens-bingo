workflow "Update audio files" {
  on = "check_run"
  resolves = ["Update files"]
}

action "Update files" {
  uses = "actions/gcloud/auth@master"
  secrets = ["GCLOUD_AUTH"]
}
