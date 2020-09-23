"""
Written by Matteo Dunnhofer - 2020

Script to run experiements with the GOT-10k framework
"""
import sys
sys.path.insert(0, '..')
import argparse
from got10k.experiments import *
from Trackers import Tracker_got10k


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', help='Name of the dataset to test on', type=str)
    parser.add_argument('--tracker', help='Tracker to run, either A3CT, A3CTD or A3CTDF')
    #parser.add_argument('--use-results', help='Use pre-computed results and not run trackers', action="store_true")
    parser.add_argument('--visualize', help='Visualize predictions while testing', action="store_true")
    args = parser.parse_args()

    if 'TRAS' in args.tracker:
        from config_track_accv import Configuration
    else:
        from config_track_iccvw import Configuration

    cfg = Configuration()

    base_data_path = cfg.DATA_PATH

    # setup tracker
    tracker = Tracker_got10k(args.tracker, cfg)

    # setup experiments
    if args.dataset == 'GOT-10k-val':
        e = ExperimentGOT10k(base_data_path + 'GOT-10k',
            result_dir= base_data_path + 'results',
            report_dir= base_data_path + 'reports',
            subset='val')
    elif args.dataset == 'GOT-10k-test':
        e = ExperimentGOT10k(base_data_path + 'GOT-10k',
            result_dir= base_data_path + 'results',
            report_dir= base_data_path + 'reports',
            subset='test')
    elif 'OTB' in args.dataset:
        version = int(''.join(list(filter(str.isdigit, args.dataset))))
        e = ExperimentOTB(base_data_path + 'OTB', version=version,
            result_dir= base_data_path + 'results',
            report_dir= base_data_path + 'reports')
    elif 'VOT' in args.dataset:
        version = int(''.join(list(filter(str.isdigit, args.dataset))))
        e = ExperimentVOT(base_data_path + 'VOT/'+str(version), version=version,
            result_dir= base_data_path + 'results',
            report_dir= base_data_path + 'reports')
    elif args.dataset == 'UAV123':
        e = ExperimentUAV123(base_data_path + 'UAV123', version='UAV123',
            result_dir= base_data_path + 'results',
            report_dir= base_data_path + 'reports')
    elif args.dataset == 'TempleColor128':
        e = ExperimentTColor128(base_data_path + 'Temple-color-128',
            result_dir=base_data_path + 'results',
            report_dir=base_data_path + 'reports')
    elif args.dataset == 'LaSOT':
        e = ExperimentLaSOT(base_data_path + 'LaSOTBenchmark',
            result_dir=base_data_path + 'results',
            report_dir=base_data_path + 'reports')


    # run tracking experiments and report performance
    e.run(tracker, visualize=args.visualize)
    e.report([tracker.name])
