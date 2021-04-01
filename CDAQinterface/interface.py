import nidaqmx

# system = nidaqmx.system.System.local()
# print(system.driver_version)
# for device in system.devices:
#     print(device)
#     for channel in device.ai_physical_chans:
#         print(channel)
#         with nidaqmx.Task() as task:
#             task.ai_channels.add_ai_voltage_chan(channel.name)
#             print(task.read(number_of_samples_per_channel=1))


class DAQ_Agent:
    def __init__(self):
        self.system = nidaqmx.system.System.local()
    def print_driver_version(self):
        print(self.system.driver_version)
    def take_voltage_samples(self, device, channel, num_samples):
        with nidaqmx.Task() as task:
            task.ai_channels.add_ai_voltage_chan(device + "/" + channel)
            return task.read(number_of_samples_per_channel = num_samples)