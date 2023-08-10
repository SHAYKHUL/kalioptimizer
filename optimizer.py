import os
import subprocess
import shutil
import threading
import resource
import multiprocessing

def disable_unneeded_services():
    print("Disabling unnecessary services...")
    services_to_disable = [
        'apache2', 'bluetooth', 'cups', 'smbd', 'winbind', 'rpcbind', 'openvpn', 'telnet'
    ]
    
    for service in services_to_disable:
        try:
            subprocess.run(f'sudo systemctl stop {service}', shell=True)
            subprocess.run(f'sudo systemctl disable {service}', shell=True)
            print(f"Disabled service: {service}")
        except Exception as e:
            print(f"Error disabling service: {service} - {e}")

def optimize_network_settings():
    print("Optimizing network settings...")
    try:
        subprocess.run('sudo sysctl -w net.ipv4.tcp_fastopen=3', shell=True)
        subprocess.run('sudo sysctl -w net.ipv4.tcp_rmem="4096 87380 33554432"', shell=True)
        subprocess.run('sudo sysctl -w net.ipv4.tcp_wmem="4096 65536 33554432"', shell=True)
        subprocess.run('sudo sysctl -w net.core.rmem_max=33554432', shell=True)
        subprocess.run('sudo sysctl -w net.core.wmem_max=33554432', shell=True)
        subprocess.run('sudo sysctl -w net.core.netdev_max_backlog=10000', shell=True)
        print("Network settings optimized.")
    except Exception as e:
        print(f"Error optimizing network settings: {e}")

def tune_file_system():
    print("Tuning file system for better performance...")
    try:
        # Enable TRIM for SSDs
        subprocess.run('sudo fstrim -av', shell=True)
        print("File system tuned.")
        subprocess.run('sudo tune2fs -o journal_data_writeback /dev/sda1', shell=True)
        print("File system tuned.")
    except Exception as e:
        print(f"Error tuning file system: {e}")

def kernel_optimization():
    print("Applying kernel optimization...")
    try:
        subprocess.run('echo 0 | sudo tee /proc/sys/kernel/nmi_watchdog', shell=True)
        subprocess.run('echo 0 | sudo tee /proc/sys/kernel/numa_balancing', shell=True)
        print("Kernel optimized.")
        subprocess.run('echo "vm.dirty_writeback_centisecs=1500" | sudo tee -a /etc/sysctl.conf', shell=True)
        subprocess.run('echo "net.core.somaxconn=65535" | sudo tee -a /etc/sysctl.conf', shell=True)
        subprocess.run('echo "net.ipv4.tcp_max_syn_backlog=65535" | sudo tee -a /etc/sysctl.conf', shell=True)
        subprocess.run('echo "net.ipv4.tcp_max_tw_buckets=2000000" | sudo tee -a /etc/sysctl.conf', shell=True)
        subprocess.run('echo "net.ipv4.tcp_tw_reuse=1" | sudo tee -a /etc/sysctl.conf', shell=True)
        subprocess.run('echo "net.ipv4.ip_local_port_range=1024 65535" | sudo tee -a /etc/sysctl.conf', shell=True)
        subprocess.run('sudo sysctl -p', shell=True)
        print("Additional kernel parameters optimized.")
    except Exception as e:
        print(f"Error applying kernel optimization: {e}")

def cpu_frequency_governor():
    print("Setting CPU frequency governor for performance...")
    try:
        subprocess.run('echo performance | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor', shell=True)
        print("CPU frequency governor set to performance.")
    except Exception as e:
        print(f"Error setting CPU frequency governor: {e}")

def enable_ksm():
    print("Enabling Kernel Samepage Merging (KSM)...")
    try:
        subprocess.run('echo 1 | sudo tee /sys/kernel/mm/ksm/run', shell=True)
        print("KSM enabled.")
    except Exception as e:
        print(f"Error enabling KSM: {e}")

def optimize_gpu_settings():
    print("Optimizing GPU settings...")
    try:
        subprocess.run('nvidia-smi --auto-boost-default=0', shell=True)  # Disable GPU auto-boost
        print("GPU settings optimized.")
    except Exception as e:
        print(f"Error optimizing GPU settings: {e}")


def clean_temporary_files():
    print("Cleaning temporary files...")
    temp_folders = [
        '/tmp', '/var/tmp', '/var/crash'
    ]
    
    for folder in temp_folders:
        try:
            shutil.rmtree(folder, ignore_errors=True)
            print(f"Deleted: {folder}")
        except Exception as e:
            print(f"Error deleting folder: {folder} - {e}")

def enable_zswap():
    print("Enabling zswap for better memory management...")
    try:
        subprocess.run('echo 1 | sudo tee /sys/module/zswap/parameters/enabled', shell=True)
        print("zswap enabled.")
    except Exception as e:
        print(f"Error enabling zswap: {e}")

def configure_swappiness():
    print("Configuring swappiness for better memory usage...")
    try:
        subprocess.run('echo 1 | sudo tee /proc/sys/vm/swappiness', shell=True)
        subprocess.run('echo 10 | sudo tee /proc/sys/vm/vfs_cache_pressure', shell=True)
        print("Swappiness and vfs_cache_pressure configured.")
    except Exception as e:
        print(f"Error configuring swappiness: {e}")

def optimize_disk_i_o():
    print("Optimizing disk I/O for better performance...")
    try:
        subprocess.run('echo deadline | sudo tee /sys/block/sda/queue/scheduler', shell=True)
        subprocess.run('sudo hdparm -a 512 /dev/sda', shell=True)  # Set read-ahead
        subprocess.run('sudo hdparm -W1 /dev/sda', shell=True)     # Enable write-caching
        print("Disk I/O optimized.")
    except Exception as e:
        print(f"Error optimizing disk I/O: {e}")

def set_process_priority():
    print("Setting process priority for optimal performance...")
    try:
        os.nice(-20)  # Set the process priority to highest
        print("Process priority set.")
    except Exception as e:
        print(f"Error setting process priority: {e}")

def limit_memory_usage():
    print("Limiting memory usage for better performance...")
    try:
        soft_limit = hard_limit = 2048 * 2048 * 2048  # 2 GB
        resource.setrlimit(resource.RLIMIT_DATA, (soft_limit, hard_limit))
        print("Memory usage limited.")
    except Exception as e:
        print(f"Error limiting memory usage: {e}")

def set_cpu_affinity():
    print("Setting CPU affinity for optimal performance...")
    try:
        cpu_count = multiprocessing.cpu_count()
        for i in range(cpu_count):
            os.sched_setaffinity(0, [i])
        print("CPU affinity set.")
    except Exception as e:
        print(f"Error setting CPU affinity: {e}")

def lock_memory_pages():
    print("Locking memory pages for improved security and performance...")
    try:
        pagesize = resource.getpagesize()
        memlock_limit = 1024 * 1024 * 1024  # 1 GB
        memlock_limit = memlock_limit // pagesize * pagesize
        resource.setrlimit(resource.RLIMIT_MEMLOCK, (memlock_limit, memlock_limit))
        print("Memory pages locked.")
    except Exception as e:
        print(f"Error locking memory pages: {e}")

def optimize_storage():
    print("Optimizing storage for better performance and space usage...")
    try:
        subprocess.run('sudo fstrim -av', shell=True)  # Trim filesystems
        subprocess.run('sudo tune2fs -o journal_data_writeback /dev/sda1', shell=True)  # Set ext4 writeback mode
        subprocess.run('sudo hdparm -B 128 /dev/sda', shell=True)  # Set aggressive power management
        print("Storage optimized.")
    except Exception as e:
        print(f"Error optimizing storage: {e}")

#advanced optimizations
def optimize_irq_affinity():
    print("Optimizing IRQ affinity for better hardware utilization...")
    try:
        subprocess.run('sudo irqbalance --oneshot', shell=True)
        print("IRQ affinity optimized.")
    except Exception as e:
        print(f"Error optimizing IRQ affinity: {e}")

def transparent_huge_pages_optimization():
    print("Fine-tuning Transparent Huge Pages for memory performance...")
    try:
        subprocess.run('echo "always" | sudo tee /sys/kernel/mm/transparent_hugepage/enabled', shell=True)
        subprocess.run('echo "1500" | sudo tee /sys/kernel/mm/transparent_hugepage/khugepaged/scan_sleep_millisecs', shell=True)
        print("Transparent Huge Pages fine-tuned.")
    except Exception as e:
        print(f"Error fine-tuning Transparent Huge Pages: {e}")

def enhance_network_security():
    print("Enhancing network security settings...")
    try:
        subprocess.run('sudo sysctl -w net.ipv4.conf.all.rp_filter=1', shell=True)
        subprocess.run('sudo sysctl -w net.ipv4.tcp_syncookies=1', shell=True)
        subprocess.run('sudo sysctl -w net.ipv4.icmp_echo_ignore_broadcasts=1', shell=True)
        subprocess.run('sudo sysctl -w net.ipv4.icmp_ignore_bogus_error_responses=1', shell=True)
        print("Network security settings enhanced.")
    except Exception as e:
        print(f"Error enhancing network security settings: {e}")

def optimize_swapiness():
    print("Fine-tuning swappiness and memory management...")
    try:
        subprocess.run('echo 5 | sudo tee /proc/sys/vm/swappiness', shell=True)
        subprocess.run('echo 100 | sudo tee /proc/sys/vm/dirty_ratio', shell=True)
        subprocess.run('echo 20 | sudo tee /proc/sys/vm/dirty_background_ratio', shell=True)
        print("Swappiness and memory management fine-tuned.")
    except Exception as e:
        print(f"Error fine-tuning swappiness and memory management: {e}")

def huge_pages_optimization():
    print("Enabling Huge Pages for memory-intensive applications...")
    try:
        subprocess.run('echo 1024 | sudo tee /proc/sys/vm/nr_hugepages', shell=True)
        subprocess.run('echo "vm.nr_overcommit_hugepages=2" | sudo tee -a /etc/sysctl.conf', shell=True)
        print("Huge Pages enabled.")
    except Exception as e:
        print(f"Error enabling Huge Pages: {e}")
        

def more_advanced_optimizations():
    print("Applying advanced optimizations...")

    # Power Management Settings
    try:
        subprocess.run('sudo powertop --auto-tune', shell=True)
        print("Power management settings optimized.")
    except Exception as e:
        print(f"Error optimizing power management settings: {e}")

    # Transparent Huge Pages Configuration
    try:
        subprocess.run('echo "never" | sudo tee /sys/kernel/mm/transparent_hugepage/enabled', shell=True)
        print("Transparent Huge Pages disabled.")
    except Exception as e:
        print(f"Error disabling Transparent Huge Pages: {e}")

    # IRQ Balancing
    try:
        subprocess.run('sudo systemctl start irqbalance', shell=True)
        print("IRQ balancing started.")
    except Exception as e:
        print(f"Error starting IRQ balancing: {e}")

    # SystemD Journal Configuration
    try:
        with open('/etc/systemd/journald.conf', 'a') as conf_file:
            conf_file.write("\nSystemMaxUse=500M\n")  # Example setting
        print("SystemD journal configuration updated.")
    except Exception as e:
        print(f"Error updating SystemD journal configuration: {e}")

    # Kernel Parameters
    try:
        subprocess.run('echo "vm.swappiness=1" | sudo tee -a /etc/sysctl.conf', shell=True)
        subprocess.run('echo "net.ipv4.tcp_sack=1" | sudo tee -a /etc/sysctl.conf', shell=True)
        subprocess.run('echo "net.core.netdev_max_backlog=5000" | sudo tee -a /etc/sysctl.conf', shell=True)
        subprocess.run('sudo sysctl -p', shell=True)
        print("Kernel parameters optimized.")
    except Exception as e:
        print(f"Error optimizing kernel parameters: {e}")
    
    # ... (more advanced optimizations)
    try:
        optimize_irq_affinity()
        transparent_huge_pages_optimization()
        enhance_network_security()
        optimize_swapiness()
        huge_pages_optimization()
        print("Additional advanced optimizations applied.")
    except Exception as e:
        print(f"Error applying additional advanced optimizations: {e}")

    print("Advanced optimizations applied.")

def additional_advanced_optimizations():
    print("Applying additional advanced optimizations...")

    # Kernel and System Parameters
    try:
        subprocess.run('echo "vm.dirty_ratio=5" | sudo tee -a /etc/sysctl.conf', shell=True)
        subprocess.run('echo "vm.dirty_background_ratio=3" | sudo tee -a /etc/sysctl.conf', shell=True)
        subprocess.run('echo "vm.swappiness=1" | sudo tee -a /etc/sysctl.conf', shell=True)
        subprocess.run('echo "vm.vfs_cache_pressure=50" | sudo tee -a /etc/sysctl.conf', shell=True)
        subprocess.run('sudo sysctl -p', shell=True)
        print("Kernel and system parameters fine-tuned.")
    except Exception as e:
        print(f"Error fine-tuning kernel and system parameters: {e}")

    # Disk Scheduler Optimization
    try:
        subprocess.run('echo "noop" | sudo tee /sys/block/sda/queue/scheduler', shell=True)
        print("Disk scheduler optimized.")
    except Exception as e:
        print(f"Error optimizing disk scheduler: {e}")

    # Power Management Tweaks
    try:
        subprocess.run('echo "1500" | sudo tee /proc/sys/vm/dirty_writeback_centisecs', shell=True)
        print("Power management tweaks applied.")
    except Exception as e:
        print(f"Error applying power management tweaks: {e}")

    # Security Hardening
    try:
        subprocess.run('sudo sysctl -w kernel.randomize_va_space=2', shell=True)
        print("Security hardening settings applied.")
    except Exception as e:
        print(f"Error applying security hardening settings: {e}")

    # SystemD Service Optimization
    try:
        subprocess.run('sudo systemctl disable atd', shell=True)
        print("Unnecessary services disabled.")
    except Exception as e:
        print(f"Error disabling unnecessary services: {e}")

    print("Additional advanced optimizations applied.")
    
    
#This functoin not needed here.. we add this in kalioptimizer
'''def main():
    print("Starting advanced Linux system optimization...")
    
    optimization_threads = [
        threading.Thread(target=disable_unneeded_services),
        threading.Thread(target=optimize_network_settings),
        threading.Thread(target=tune_file_system),
        threading.Thread(target=kernel_optimization),
        threading.Thread(target=cpu_frequency_governor),
        threading.Thread(target=optimize_gpu_settings),
        threading.Thread(target=clean_temporary_files),
        threading.Thread(target=enable_zswap),
        threading.Thread(target=configure_swappiness),
        threading.Thread(target=optimize_disk_i_o),
        threading.Thread(target=set_process_priority),
        threading.Thread(target=limit_memory_usage),
        threading.Thread(target=set_cpu_affinity),
        threading.Thread(target=lock_memory_pages),
        threading.Thread(target=optimize_storage),
        threading.Thread(target=optimize_irq_affinity),
        threading.Thread(target=transparent_huge_pages_optimization),
        threading.Thread(target=enhance_network_security),
        threading.Thread(target=optimize_swappiness),
        threading.Thread(target=huge_pages_optimization),
        threading.Thread(target=more_advanced_optimizations),
        threading.Thread(target=additional_advanced_optimizations),
    ]
    
    for thread in optimization_threads:
        thread.start()
    
    for thread in optimization_threads:
        thread.join()
    
    print("Advanced Linux system optimization complete.")


if __name__ == "__main__":
    main()'''
