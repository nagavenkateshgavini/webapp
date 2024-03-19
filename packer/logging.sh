set -e

echo "Started Installation of fluent bit OPs agent"
echo "Printing current dir..."
echo `pwd`

curl -sSO https://dl.google.com/cloudagents/add-google-cloud-ops-agent-repo.sh
sudo bash add-google-cloud-ops-agent-repo.sh --also-install

sleep 10

# Configures Ops Agent to collect telemetry from the app and restart Ops Agent.

# Configure the Ops Agent.
sudo tee /etc/google-cloud-ops-agent/config.yaml > /dev/null << EOF
logging:
  receivers:
    webapp-receiver:
      type: files
      include_paths:
        - $LOG_FILE
      record_log_file_path: true
  processors:
    webapp-processor:
      type: parse_json
      time_key: time
      time_format: "%Y-%m-%dT%H:%M:%S.%L%Z"
    move_severity:
      type: modify_fields
      fields:
        severity:
          move_from: jsonPayload.level
  service:
    pipelines:
      default_pipeline:
        receivers: [webapp-receiver]
        processors: [webapp-processor, move_severity]

EOF

sudo service google-cloud-ops-agent restart
sleep 60
