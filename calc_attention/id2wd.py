#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import json
import argparse


def main(args):
    input_tokens = []
    with open(args.input_file, 'r') as f:
        input_tokens = json.load(f)

    vocab_file = []
    with open(args.vocab_file, 'r') as f:
        vocab_file = f.readlines()

    json_file = []
    for tokens in input_tokens:
        text = []
        for token in tokens['input_ids']:
            text.append(vocab_file[int(token)].strip('\n'))
        json_file.append({'sentence': text})

    with open(args.save_file, 'w') as f:
        json.dump(json_file, f)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                prog='id2wd',
                usage='idからトークンに変換',
                add_help=True,
                )
    parser.add_argument('-f',
                        '--input_file',
                        default='../bert_input_ids/save_ids.json',
                        help='入力用のデータ')
    parser.add_argument('-v',
                        '--vocab_file',
                        default='../bert_input_ids/vocab.txt',
                        help='vocab file')
    parser.add_argument('-s',
                        '--save_file',
                        default='../bert_input_ids/features.json',
                        help='保存先')
    args = parser.parse_args()
    main(args)
