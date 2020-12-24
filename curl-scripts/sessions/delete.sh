#!/bin/bash

curl "http://localhost:8000/sessions/${ID}" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
