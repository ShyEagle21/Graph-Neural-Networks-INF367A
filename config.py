from os.path import join

# Paths
data_path = "data"
figs_path = "figs"
docs_path = "docs"
checkpoints_path = "checkpoints"

# Filenames
data_file_zip = join(data_path, "traffic_data.zip")
data_file_pkl = join(data_path, "traffic_data.pkl")
stations_data_file = join(data_path, "traffic_stations.csv")
summary_table_file = join(docs_path, "data_summary_table.md")
time_series_file = join(data_path, "time_series_data.pkl")
train_data_file = join(data_path, "time_series_train.pkl")
val_data_file = join(data_path, "time_series_val.pkl")
test_data_file = join(data_path, "time_series_test.pkl")

# Pre-processing
min_number_of_observations = 1500   # Drop stations having too few observations
val_fraction = 0.15                 # Fraction of data to use for validation data
test_fraction = 0.15                # Fraction of data to use for test data
normalize_data = None               # "minmax" : scale to [0,1], "normal" : use z-scores, None : no normalization

# Training 
num_workers = 8                     # Number of workers to use with dataloader.
device = "cuda:4"                   # Device for PyTorch to use. Can be "cpu" or "cuda:n".
validations_per_epoch = 4           # How many time to do validation per epoch.

# Baseline model
config_baseline = {}
config_baseline["name"] = "Baseline"
config_baseline["batch_size"] = 128 
config_baseline["lr"] = 0.001
config_baseline["epochs"] = 100
config_baseline["checkpoint_file"] = join(checkpoints_path, "baseline.pth") 
config_baseline["prediction_plot_file"] = join(figs_path, "baseline_prediction_plot.png")
config_baseline["earlystop_limit"] = 15
