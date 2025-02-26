import h5py
import json

# Load the model file
with h5py.File("chest_xray_model.h5", "r+") as f:
    model_config = json.loads(f.attrs["model_config"])
    
    # Traverse and rename layers with '/'
    for layer in model_config["config"]["layers"]:
        if "name" in layer["config"]:
            layer["config"]["name"] = layer["config"]["name"].replace("/", "_")
    
    # Save back the modified configuration
    f.attrs["model_config"] = json.dumps(model_config)

print("Layer names updated successfully!")

import tensorflow as tf

model = tf.keras.models.load_model("chest_xray_model.h5", compile=False, safe_mode=False)
print("Model loaded successfully!")
model.save("chest_xray_model_fixed.h5")

