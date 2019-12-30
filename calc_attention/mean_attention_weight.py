#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json
import argparse
import numpy as np


def calc_attention_weight(atten_features):
    # (batch, heads, sequence_length, sequence_length)
    layer_sum = np.sum(atten_features, axis=0)
    layer_sum = np.divide(layer_sum, args.num_layer)

    # (batch, sequence_length, sequence_length)
    head_sum = np.sum(layer_sum, axis=1)
    head_sum = np.divide(head_sum, args.num_head)

    # (batch, sequence_length)
    token_sum = np.sum(head_sum, axis=1)
    token_sum = np.divide(token_sum, args.sequence_length)
    return token_sum


def main(args):
    features_path = args.attention_dir
    feature_list = os.listdir(features_path)
    que_json = []
    with open(args.save_json) as f:
        que_json = json.load(f)

    que_json_idx = 0
    for path in feature_list:
        # (layer, batch, heads, sequence_length, sequence_length)
        atten_features = np.load(os.path.join(features_path, path))

        attention_weight = calc_attention_weight(atten_features)

        for weight in attention_weight:
            que_json[que_json_idx]["attention_weight"] = list(np.float64(weight))
            que_json_idx += 1

    with open(args.save_json, 'w') as f:
        json.dump(que_json, f)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--num_layer',
                        default=12,
                        type=int,
                        help='bertのlayer数')
    parser.add_argument('--num_head',
                        default=12,
                        type=int,
                        help='bertのhead数')
    parser.add_argument('--sequence_length',
                        default=128,
                        type=int,
                        help='sequence_lengthの大きさ')
    parser.add_argument('--attention_dir',
                        default='../attention_weight',
                        help='入力用のデータ')
    parser.add_argument('--input_ids',
                        default='../bert_input_ids/save_ids.json',
                        help='テキストのファイル')
    parser.add_argument('-s',
                        '--save_json',
                        default='../features/features.json',
                        help='保存先')
    args = parser.parse_args()
    main(args)
