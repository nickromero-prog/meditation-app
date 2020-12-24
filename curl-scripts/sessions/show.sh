#!/bin/bash

curl "http://localhost:8000/sessions/${ID}" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
