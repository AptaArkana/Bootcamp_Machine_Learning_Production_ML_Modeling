def convert_params(config):
    for key, value in config.items():
        try:
            # Attempt to convert string numbers to floats
            config[key] = int(value)
        except ValueError:
            # Keep the original value if conversion is not possible
            pass
        except TypeError:
            pass
    return config