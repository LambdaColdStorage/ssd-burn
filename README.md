# ssd-burn
burning test for SSD


Usage
===

```bash
./ssd_burn.sh SSD_NAME NUM_ITER
python parse_results.py SSD_NAME


# Example:
./ssd_burn.sh HP_EX950_2TB_vertical_loaded 10
python parse_results.py HP_EX950_2TB_vertical_loaded
```

Note
===

The benchmark is based on [fio](https://github.com/axboe/fio). In practice, the performance of an ssd varies with the parameters used to run fio, especially so in the random read/write tasks.

We have tested a number of different parameters, from which the most reasonable settings are used for long period burning tests. Here are all different parameters we have tried:

__Sequential write__

```bash
rm fio-tempfile.dat ; fio --name TEST --eta-newline=5s --filename=fio-tempfile.dat --rw=write --blocksize=1024k --ioengine=libaio --iodepth=32 --direct=1 --numjobs=1 --size=250g --runtime=12000

HP 1250MB, SAMSUNG 1250MB (Used in burning test)
```

__Sequential read__

```bash
fio --name TEST --eta-newline=5s --filename=fio-tempfile4read.dat --rw=read --blocksize=1024k --ioengine=libaio --iodepth=32 --direct=1 --numjobs=1 --size=250g --runtime=12000

HP 3300MB, SAMSUNG 3300MB (Used in burning test)
```

__4K random write__

```bash
rm fio-tempfile.dat ; fio --name TEST --eta-newline=5s --filename=fio-tempfile.dat --rw=randwrite --blocksize=4k --ioengine=libaio --iodepth=32 --direct=1 --numjobs=1 --size=10g --runtime=180 

HP 300MB, SAMSUNG 300MB (Used in burning test)
```

```bash
rm fio-tempfile.dat ; fio --name TEST --eta-newline=5s --filename=fio-tempfile.dat --rw=randwrite --blocksize=4k --ioengine=libaio --iodepth=1 --direct=1 --numjobs=1 --size=10g --runtime=120

HP 90 MB, SAMSUNG 90 MB
```

```bash
rm fio-tempfile.dat ; fio --name TEST --eta-newline=5s --filename=fio-tempfile.dat --rw=randwrite --blocksize=4k --ioengine=libaio --iodepth=1 --direct=1 --numjobs=1 --size=10g --runtime=120 --fsync=1

HP 7000 kB, SAMSUNG 1200 kB
```

__4K random read__

```bash
fio --name TEST --eta-newline=5s --filename=fio-tempfile4read.dat --rw=randread --blocksize=4k --ioengine=libaio --iodepth=32 --direct=1 --numjobs=1 --size=10g --runtime=120

HP 550MB, SAMSUNG 800MB (Used in burning test)
```

```bash
fio --name TEST --eta-newline=5s --filename=fio-tempfile4read.dat --rw=randread --blocksize=4k --ioengine=libaio --iodepth=1 --direct=1 --numjobs=1 --size=10g --runtime=120

HP 47MB, SAMSUNG 42MB
```

Reference
===
[Mikejung's blog](https://wiki.mikejung.biz/Benchmarking)

[NVidia blog: Storage Performance Basics for Deep Learning
](https://devblogs.nvidia.com/storage-performance-basics-for-deep-learning/)
