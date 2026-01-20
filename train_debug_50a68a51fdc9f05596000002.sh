#!/bin/bash
DEVICE="cuda"
BATCH_SIZE="16"
ENTRY='main.py'
MAX_ITER=200

for TASK in task2; do
    # train image-only model (densenet201)
    #CUDA_VISIBLE_DEVICES=1 python3.9 $ENTRY --model_name "image_only_$TASK" --mode image_only --task $TASK --batch_size $BATCH_SIZE --device $DEVICE --max_iter $MAX_ITER --type "50a68a51fdc9f05596000002" --debug

    # train text-only model (bert)
    CUDA_VISIBLE_DEVICES=2 python3.9 $ENTRY --model_name "text_only_$TASK" --mode text_only --task $TASK --batch_size $BATCH_SIZE --device $DEVICE --max_iter $MAX_ITER --type "50a68a51fdc9f05596000002" --debug

    # Combined model
    #CUDA_VISIBLE_DEVICES=1 python3.9 $ENTRY --model_name "full_$TASK" --mode both --task $TASK --batch_size $BATCH_SIZE --device $DEVICE --max_iter $MAX_ITER --image_model_to_load "./output/image_only_$TASK/best.pt"  --text_model_to_load "./output/text_only_$TASK/best.pt" --type "50a68a51fdc9f05596000002" --debug
done
