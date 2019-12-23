export GLUE_DIR=GLUE
export TASK_NAME=SST-2
export BERT_PATH=/bert/Japanese_L-12_H-768_A-12_E-30_BPE_transformers/
export MAX_SEQ_LEN=128
export BATCH_SIZE=8

usage_exit() {
    echo "Usage: $0 [-t] [-e] [-d data_dir]" 1>&2
    exit 1
}

while getopts ted:h OPT
do
    case $OPT in
        t)  FLAG_T=1
            ;;
        e)  FLAG_E=1
            ;;
        d)  DATA_DIR=$OPTARG
	    ;;
        h)  usage_exit
            ;;
        \?) usage_exit
            ;;
    esac
done
shift $((OPTIND - 1))

if [[ $FLAG_T -eq 1 ]]; then
    python jp_run_classifier.py \
        --model_type bert \
        --model_name_or_path $BERT_PATH \
        --task_name $TASK_NAME \
        --do_train \
        --data_dir $DATA_DIR \
        --max_seq_length $MAX_SEQ_LEN \
        --per_gpu_train_batch_size=$BATCH_SIZE \
        --learning_rate 2e-5 \
        --num_train_epochs 3.0 \
        --output_dir tmp/$TASK_NAME/ \
        --save_steps 1000000 \
        --overwrite_output_dir
fi

if [[ $FLAG_E -eq 1 ]]; then
    python jp_run_classifier.py \
        --model_type bert \
        --model_name_or_path $BERT_PATH \
        --task_name $TASK_NAME \
        --do_eval \
        --data_dir $DATA_DIR \
        --max_seq_length $MAX_SEQ_LEN \
        --per_gpu_eval_batch_size=$BATCH_SIZE \
        --output_dir tmp/$TASK_NAME/ \
        --save_steps 1000000 \
        --overwrite_output_dir \
        --attention_visualize 
fi
