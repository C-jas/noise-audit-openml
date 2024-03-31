# noise-audit-openml
Repository meiner Bachelorarbeit: Noise - Die Verrauschung von Algorithmen. Enthält alle Programme für das Durchführen eines Noise-Audits auf OpenML

regression_flow_finder hat alle Flows auf einer Task gefunden, und angegeben, wieviele Runs er auf der Task hat.
list_storage enthält die von regression_flow_finder.py produzierten Listen je nach Task.
unique_run_of_flow_finder hat herausgefunden wieviele verschiedene RMSE, und damit wieviele unterschiedliche Runs es von einem Flow auf einer Task gab.
Flow_17357_info ruft alle informationen des Flows über die API ab.
noise_audit_flow_17357 führt ein Noise-Audit für diesen Flow auf Task 2295 durch und gibt dies als Latextabellencode aus.
pattern_noise_test prüft die Richtigkeit der Formeln, die für Pattern-Noise aufgestellt wurden.
