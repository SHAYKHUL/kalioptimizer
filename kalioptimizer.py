# Developer: [shaykhul]
# Script: Linux System Optimizer
# Version: 1.0
# Date: [Date]
# Description: This script provides a menu-driven approach to optimize a Linux system.
#!/usr/bin/env python3
import time
import threading
from optimizer import*
#from kali_optimizer import optimize_system

def print_banner():
    banner = "\033[32m" + """
  _  __     _ _  ____        _   _           _              
 | |/ /    | (_)/ __ \      | | (_)         (_)             
 | ' / __ _| |_| |  | |_ __ | |_ _ _ __ ___  _ _______ _ __ 
 |  < / _` | | | |  | | '_ \| __| | '_ ` _ \| |_  / _ \ '__|
 | . \ (_| | | | |__| | |_) | |_| | | | | | | |/ /  __/ |   
 |_|\_\__,_|_|_|\____/| .__/ \__|_|_| |_| |_|_/___\___|_|   
                      | |                                   
                      |_|                                   

            Contact: contact@algolizen.com
            Website: www.algolizen.com                                                       
    """ + "\033[0m"
    print(banner)

def basic_optimizations():
    # List of functions corresponding to basic optimizations
    optimization_functions = [
        disable_unneeded_services,
        optimize_network_settings,
        clean_temporary_files,
    ]
    
    for func in optimization_functions:
        func()

def advanced_optimizations():
    # List of functions corresponding to advanced optimizations
    optimization_functions = [
        enable_zswap,
        configure_swappiness,
        optimize_disk_i_o,
        set_process_priority,
        limit_memory_usage,
        set_cpu_affinity,
        lock_memory_pages,
        tune_file_system,
        kernel_optimization,
        cpu_frequency_governor,
        enable_ksm,
        optimize_gpu_settings,
        optimize_irq_affinity,
        transparent_huge_pages_optimization,
        enhance_network_security,
        optimize_swapiness,
        huge_pages_optimization,
        more_advanced_optimizations,
        additional_advanced_optimizations
        
    ]
    
    for func in optimization_functions:
        func()

def full_optimizations():
    optimization_functions = [
        basic_optimizations,
        advanced_optimizations,
        
    ]
    
    for func in optimization_functions:
        func()

def about():
    info = '''
    # Developer: shaykhul
    # Script: Linux System Optimizer
    # Version: 1.0
    # Date: 10
    # Description: This script provides a menu-driven approach to optimize a Linux system.
        Copyright © 2023 Algolizen. All rights reserved.

    '''
    print(info)

def main():
    print_banner()
    print("Starting Linux system optimization...")
    print("Options:")
    print("1. Basic Optimization")
    print("2. Advanced Optimization")
    print("3. Full system Optimization")
    print("4. About")
    print("0. Exit")
    
    option = input("Enter the option number: ")
    
    if option == "1":
        print("starting basic optimization..")
        time.sleep(3)
        basic_optimizations()
        print("Basic optimization complete")
        c = input("Do you want goto main menu or close Y/n: ")
        if c == "Y":
            return main()
        else:
            exit()
    elif option == "2":
        advanced_optimizations()
        print("Linux advanced system optimization completed.")
    elif option == "3":
        full_optimizations()
        print("Linux full system optimization completed.")
    elif option == "0":
        exit()
    elif option == "4":
        return about()
    else:
        print("Invalid option selected.")
        return
    
    

if __name__ == "__main__":
    main()
