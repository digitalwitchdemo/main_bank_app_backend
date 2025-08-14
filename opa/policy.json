package docker.compliance

# 1. Approved base image registry
deny[msg] {
    not startswith(input.base_image, "registry.bank.local/")
    not startswith(input.base_image, "gcr.io/verified/")
    msg := sprintf("Base image %v is not from an approved registry", [input.base_image])
}

# 2. No root user
deny[msg] {
    input.user == "root"
    msg := "Dockerfile must not run as root user"
}

# 3. Mandatory non-root user
deny[msg] {
    not input.user
    msg := "No USER instruction found — a non-root user must be defined"
}

# 4. No latest tag
deny[msg] {
    endswith(input.base_image, ":latest")
    msg := "Base image tag 'latest' is not allowed — pin to a specific version"
}

# 5. Security updates
deny[msg] {
    not any([cmd | cmd := input.run_commands[_]; contains(cmd, "apt-get update")])
    msg := "Dockerfile must include security updates (e.g., apt-get update && apt-get upgrade)"
}
