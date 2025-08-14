#!/usr/bin/env bash
set -e

DOCKERFILE_PATH=${1:-Dockerfile}

# Extract base image
BASE_IMAGE=$(grep -i '^FROM ' "$DOCKERFILE_PATH" | head -n1 | awk '{print $2}')

# Extract USER instruction
USER_LINE=$(grep -i '^USER ' "$DOCKERFILE_PATH" | tail -n1 | awk '{print $2}')

# Extract all RUN commands
RUN_COMMANDS=$(grep -i '^RUN ' "$DOCKERFILE_PATH" | sed 's/^RUN //' | jq -R -s -c 'split("\n")[:-1]')

# Build JSON
jq -n \
  --arg base_image "$BASE_IMAGE" \
  --arg user "$USER_LINE" \
  --argjson run_commands "$RUN_COMMANDS" \
  '{base_image: $base_image, user: $user, run_commands: $run_commands}'
