import openml

#ruft alle informationen des Flows über die API ab
Flow = openml.flows.get_flow(17357)

print(Flow.name)
print(Flow.description)
model = Flow.model
print(Flow.external_version)
print(Flow.language)
print(Flow.dependencies)
print(Flow.version)