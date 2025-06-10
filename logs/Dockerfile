FROM fluent/fluentd:v1.16-debian

USER root

RUN gem install fluent-plugin-grafana-loki --no-document

COPY fluent.conf /fluentd/etc/

USER fluent
