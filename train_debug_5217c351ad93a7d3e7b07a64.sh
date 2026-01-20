#!/bin/bash
DEVICE="cuda"
BATCH_SIZE="16"
ENTRY='main.py'
MAX_ITER=60

for TASK in task2; do
    # train image-only model (densenet201)
    CUDA_VISIBLE_DEVICES=0 python3.9 $ENTRY --model_name "image_only_$TASK" --mode image_only --task $TASK --batch_size $BATCH_SIZE --device $DEVICE --max_iter $MAX_ITER --type "5217c351ad93a7d3e7b07a64" --debug

    # train text-only model (bert)
    CUDA_VISIBLE_DEVICES=0 python3.9 $ENTRY --model_name "text_only_$TASK" --mode text_only --task $TASK --batch_size $BATCH_SIZE --device $DEVICE --max_iter $MAX_ITER --type "5217c351ad93a7d3e7b07a64" --debug

    # Combined model
    CUDA_VISIBLE_DEVICES=0 python3.9 $ENTRY --model_name "full_$TASK" --mode both --task $TASK --batch_size $BATCH_SIZE --device $DEVICE --max_iter $MAX_ITER --image_model_to_load "./output/image_only_$TASK/best.pt"  --text_model_to_load "./output/text_only_$TASK/best.pt" --type "5217c351ad93a7d3e7b07a64" --debug
done
