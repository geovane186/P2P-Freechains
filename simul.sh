#DIA 01 -----------------------------------------------------------------------

#HOST 1 (8330)
#freechains-host start /tmp/myhost
freechains-host now '2021-11-04 19:00:00.000'
key=$(freechains crypto pubpvt 'first-password');
pubKey=$(echo $key | cut -d' ' -f1);
priKey=$(echo $key | cut -d' ' -f2);
freechains chains join '#Algebra' $pubKey
freechains chain '#Algebra' post --sign=$priKey file 'q_u1.pdf'

#DIA 02 -----------------------------------------------------------------------

#HOST 1 (8330)
freechains-host now '2021-11-05 19:00:00.000'

#HOST 2 (8331)
freechains-host --port=8331 start /tmp/othost&
freechains-host --port=8331 now '2021-11-05 19:05:00.000'
key=$(freechains crypto pubpvt 'second-password');
pubKey2=$(echo $key | cut -d' ' -f1);
priKey2=$(echo $key | cut -d' ' -f2);
freechains --host=localhost:8331 chains join '#Algebra' $pubKey
freechains --host=localhost:8331 peer localhost:8330 recv '#Algebra'
POST_U2=$(freechains --host=localhost:8331 chain '#Algebra' post --sign=$priKey2 file 'q_u2.pdf');

#HOST 1 (8330)
freechains --host=localhost:8330 peer localhost:8331 recv '#Algebra'
freechains chain '#Algebra' like $POST_U2 --sign=$priKey

#DIA 03 -----------------------------------------------------------------------

#HOST 1 (8330)
freechains-host now '2021-11-06 19:00:00.000'

#HOST 2 (8331)
freechains-host --port=8331 now '2021-11-06 19:05:00.000'

#HOST 3 (8332)
freechains-host --port=8332 start /tmp/tohost&
freechains-host --port=8332 now '2021-11-06 19:10:00.000'
key=$(freechains crypto pubpvt 'third-password');
pubKey3=$(echo $key | cut -d' ' -f1);
priKey3=$(echo $key | cut -d' ' -f2);
freechains --host=localhost:8332 chains join '#Algebra' $pubKey
freechains --host=localhost:8332 peer localhost:8330 recv '#Algebra'
freechains --host=localhost:8332 peer localhost:8331 recv '#Algebra'
POST_U3=$(freechains --host=localhost:8332 chain '#Algebra' post --sign=$priKey3 file 'q_u3.pdf');

#HOST 1 (8330)
freechains --host=localhost:8330 peer localhost:8332 recv '#Algebra'
freechains chain '#Algebra' like $POST_U3 --sign=$priKey

freechains chain '#Algebra' reps $pubKey
freechains chain '#Algebra' reps $pubKey2
freechains chain '#Algebra' reps $pubKey3

#DIA 04 -----------------------------------------------------------------------

#HOST 1 (8330)
freechains-host now '2021-11-07 19:00:00.000'

#HOST 2 (8331)
freechains-host --port=8331 now '2021-11-07 19:05:00.000'

#HOST 3 (8332)
freechains-host --port=8332 now '2021-11-07 19:10:00.000'

#HOST 1 (8330)
freechains --host=localhost:8330 peer localhost:8331 recv '#Algebra'
freechains --host=localhost:8330 peer localhost:8332 recv '#Algebra'
POST_U1=$(freechains chain '#Algebra' post --sign=$priKey file 'q_u1.pdf');

#HOST 2 (8331)
freechains --host=localhost:8331 peer localhost:8330 recv '#Algebra'
freechains --host=localhost:8331 peer localhost:8332 recv '#Algebra'
POST_U2=$(freechains --host=localhost:8331 chain '#Algebra' post --sign=$priKey2 file 'q_u2.pdf');
freechains --host=localhost:8331 chain '#Algebra' like $POST_U1 --sign=$priKey2

#HOST 3 (8332)
freechains --host=localhost:8332 peer localhost:8330 recv '#Algebra'
freechains --host=localhost:8332 peer localhost:8331 recv '#Algebra'
POST_U3=$(freechains --host=localhost:8332 chain '#Algebra' post --sign=$priKey3 file 'q_u3.pdf');
freechains --host=localhost:8332 chain '#Algebra' like $POST_U1 --sign=$priKey3

#HOST 1 (8330)
freechains --host=localhost:8330 peer localhost:8331 recv '#Algebra'
freechains --host=localhost:8330 peer localhost:8332 recv '#Algebra'
freechains chain '#Algebra' like $POST_U2 --sign=$priKey
freechains chain '#Algebra' like $POST_U3 --sign=$priKey

freechains chain '#Algebra' reps $pubKey
freechains chain '#Algebra' reps $pubKey2
freechains chain '#Algebra' reps $pubKey3

#DIA 05 -----------------------------------------------------------------------

#HOST 1 (8330)
freechains-host now '2021-11-08 19:00:00.000'

#HOST 2 (8331)
freechains-host --port=8331 now '2021-11-08 19:05:00.000'

#HOST 3 (8332)
freechains-host --port=8332 now '2021-11-08 19:10:00.000'

#HOST 1 (8330)
freechains --host=localhost:8330 peer localhost:8331 recv '#Algebra'
freechains --host=localhost:8330 peer localhost:8332 recv '#Algebra'
POST_U1=$(freechains chain '#Algebra' post --sign=$priKey file 'q_u1.pdf');

#HOST 2 (8331)
freechains --host=localhost:8331 peer localhost:8330 recv '#Algebra'
freechains --host=localhost:8331 peer localhost:8332 recv '#Algebra'
POST_U2=$(freechains --host=localhost:8331 chain '#Algebra' post --sign=$priKey2 file 'q_u2.pdf');
freechains --host=localhost:8331 chain '#Algebra' like $POST_U1 --sign=$priKey2

#HOST 3 (8332)
freechains --host=localhost:8332 peer localhost:8330 recv '#Algebra'
freechains --host=localhost:8332 peer localhost:8331 recv '#Algebra'
POST_U3=$(freechains --host=localhost:8332 chain '#Algebra' post --sign=$priKey3 file 'q_u3.pdf');
freechains --host=localhost:8332 chain '#Algebra' like $POST_U1 --sign=$priKey3

#HOST 1 (8330)
freechains --host=localhost:8330 peer localhost:8331 recv '#Algebra'
freechains --host=localhost:8330 peer localhost:8332 recv '#Algebra'
freechains chain '#Algebra' like $POST_U2 --sign=$priKey
freechains chain '#Algebra' like $POST_U3 --sign=$priKey

freechains chain '#Algebra' reps $pubKey
freechains chain '#Algebra' reps $pubKey2
freechains chain '#Algebra' reps $pubKey3

#DIA 06 -----------------------------------------------------------------------

#HOST 1 (8330)
freechains-host now '2021-11-09 19:00:00.000'

#HOST 2 (8331)
freechains-host --port=8331 now '2021-11-09 19:05:00.000'

#HOST 3 (8332)
freechains-host --port=8332 now '2021-11-09 19:10:00.000'

#HOST 1 (8330)
freechains --host=localhost:8330 peer localhost:8331 recv '#Algebra'
freechains --host=localhost:8330 peer localhost:8332 recv '#Algebra'
POST_U1=$(freechains chain '#Algebra' post --sign=$priKey file 'q_u1.pdf');

#HOST 2 (8331)
freechains --host=localhost:8331 peer localhost:8330 recv '#Algebra'
freechains --host=localhost:8331 peer localhost:8332 recv '#Algebra'
POST_U2=$(freechains --host=localhost:8331 chain '#Algebra' post --sign=$priKey2 file 'q_u2.pdf');
freechains --host=localhost:8331 chain '#Algebra' like $POST_U1 --sign=$priKey2

#HOST 3 (8332)
freechains --host=localhost:8332 peer localhost:8330 recv '#Algebra'
freechains --host=localhost:8332 peer localhost:8331 recv '#Algebra'
POST_U3=$(freechains --host=localhost:8332 chain '#Algebra' post --sign=$priKey3 file 'q_u3.pdf');
freechains --host=localhost:8332 chain '#Algebra' like $POST_U1 --sign=$priKey3

#HOST 1 (8330)
freechains --host=localhost:8330 peer localhost:8331 recv '#Algebra'
freechains --host=localhost:8330 peer localhost:8332 recv '#Algebra'
freechains chain '#Algebra' like $POST_U2 --sign=$priKey
freechains chain '#Algebra' like $POST_U3 --sign=$priKey

freechains chain '#Algebra' reps $pubKey
freechains chain '#Algebra' reps $pubKey2
freechains chain '#Algebra' reps $pubKey3

#DIA 07 -----------------------------------------------------------------------

#HOST 1 (8330)
freechains-host now '2021-11-10 19:00:00.000'

#HOST 2 (8331)
freechains-host --port=8331 now '2021-11-10 19:05:00.000'

#HOST 3 (8332)
freechains-host --port=8332 now '2021-11-10 19:10:00.000'

#HOST 1 (8330)
freechains --host=localhost:8330 peer localhost:8331 recv '#Algebra'
freechains --host=localhost:8330 peer localhost:8332 recv '#Algebra'
POST_U1=$(freechains chain '#Algebra' post --sign=$priKey file 'q_u1.pdf');

#HOST 2 (8331)
freechains --host=localhost:8331 peer localhost:8330 recv '#Algebra'
freechains --host=localhost:8331 peer localhost:8332 recv '#Algebra'
POST_U2=$(freechains --host=localhost:8331 chain '#Algebra' post --sign=$priKey2 file 'q_u2.pdf');
freechains --host=localhost:8331 chain '#Algebra' like $POST_U1 --sign=$priKey2

#HOST 3 (8332)
freechains --host=localhost:8332 peer localhost:8330 recv '#Algebra'
freechains --host=localhost:8332 peer localhost:8331 recv '#Algebra'
POST_U3=$(freechains --host=localhost:8332 chain '#Algebra' post --sign=$priKey3 file 'q_u3.pdf');
freechains --host=localhost:8332 chain '#Algebra' like $POST_U1 --sign=$priKey3

#HOST 1 (8330)
freechains --host=localhost:8330 peer localhost:8331 recv '#Algebra'
freechains --host=localhost:8330 peer localhost:8332 recv '#Algebra'
freechains chain '#Algebra' like $POST_U2 --sign=$priKey
freechains chain '#Algebra' like $POST_U3 --sign=$priKey

freechains chain '#Algebra' reps $pubKey
freechains chain '#Algebra' reps $pubKey2
freechains chain '#Algebra' reps $pubKey3

#...

#DIA 45 -----------------------------------------------------------------------

#USER 3 publica post troll e começa a criticar o post do USER 1

#HOST 1 (8330)
freechains-host now '2021-12-18 19:00:00.000'

#HOST 2 (8331)
freechains-host --port=8331 now '2021-12-18 19:05:00.000'

#HOST 3 (8332)
freechains-host --port=8332 now '2021-12-18 19:10:00.000'

#HOST 1 (8330)
freechains --host=localhost:8330 peer localhost:8331 recv '#Algebra'
freechains --host=localhost:8330 peer localhost:8332 recv '#Algebra'
POST_U1=$(freechains chain '#Algebra' post --sign=$priKey file 'q_u1.pdf');

#HOST 2 (8331)
freechains --host=localhost:8331 peer localhost:8330 recv '#Algebra'
freechains --host=localhost:8331 peer localhost:8332 recv '#Algebra'
POST_U2=$(freechains --host=localhost:8331 chain '#Algebra' post --sign=$priKey2 file 'q_u2.pdf');
freechains --host=localhost:8331 chain '#Algebra' like $POST_U1 --sign=$priKey2

#HOST 3 (8332)
freechains --host=localhost:8332 peer localhost:8330 recv '#Algebra'
freechains --host=localhost:8332 peer localhost:8331 recv '#Algebra'
POST_U3=$(freechains --host=localhost:8332 chain '#Algebra' post --sign=$priKey3 file 'troll_u3.pdf');
freechains --host=localhost:8332 chain '#Algebra' dislike $POST_U1 --sign=$priKey3

#HOST 1 (8330)
freechains --host=localhost:8330 peer localhost:8331 recv '#Algebra'
freechains --host=localhost:8330 peer localhost:8332 recv '#Algebra'
freechains chain '#Algebra' like $POST_U2 --sign=$priKey
freechains chain '#Algebra' dislike $POST_U3 --sign=$priKey

freechains chain '#Algebra' reps $pubKey
freechains chain '#Algebra' reps $pubKey2
freechains chain '#Algebra' reps $pubKey3

#DIA 46 -----------------------------------------------------------------------

#HOST 1 (8330)
freechains-host now '2021-12-19 19:00:00.000'

#HOST 2 (8331)
freechains-host --port=8331 now '2021-12-19 19:05:00.000'

#HOST 3 (8332)
freechains-host --port=8332 now '2021-12-19 19:10:00.000'

#HOST 1 (8330)
freechains --host=localhost:8330 peer localhost:8331 recv '#Algebra'
freechains --host=localhost:8330 peer localhost:8332 recv '#Algebra'
POST_U1=$(freechains chain '#Algebra' post --sign=$priKey file 'q_u1.pdf');

#HOST 2 (8331)
freechains --host=localhost:8331 peer localhost:8330 recv '#Algebra'
freechains --host=localhost:8331 peer localhost:8332 recv '#Algebra'
POST_U2=$(freechains --host=localhost:8331 chain '#Algebra' post --sign=$priKey2 file 'q_u2.pdf');
freechains --host=localhost:8331 chain '#Algebra' like $POST_U1 --sign=$priKey2

#HOST 3 (8332)
freechains --host=localhost:8332 peer localhost:8330 recv '#Algebra'
freechains --host=localhost:8332 peer localhost:8331 recv '#Algebra'
POST_U3=$(freechains --host=localhost:8332 chain '#Algebra' post --sign=$priKey3 file 'troll_u3.pdf');


#HOST 1 (8330)
freechains --host=localhost:8330 peer localhost:8331 recv '#Algebra'
freechains --host=localhost:8330 peer localhost:8332 recv '#Algebra'
freechains chain '#Algebra' like $POST_U2 --sign=$priKey

freechains chain '#Algebra' reps $pubKey
freechains chain '#Algebra' reps $pubKey2
freechains chain '#Algebra' reps $pubKey3

#DIA 47 -----------------------------------------------------------------------

#HOST 1 (8330)
freechains-host now '2021-12-20 19:00:00.000'

#HOST 2 (8331)
freechains-host --port=8331 now '2021-12-20 19:05:00.000'

#HOST 3 (8332)
freechains-host --port=8332 now '2021-12-20 19:10:00.000'

#HOST 1 (8330)
freechains --host=localhost:8330 peer localhost:8331 recv '#Algebra'
freechains --host=localhost:8330 peer localhost:8332 recv '#Algebra'
POST_U1=$(freechains chain '#Algebra' post --sign=$priKey file 'q_u1.pdf');

#HOST 2 (8331)
freechains --host=localhost:8331 peer localhost:8330 recv '#Algebra'
freechains --host=localhost:8331 peer localhost:8332 recv '#Algebra'
POST_U2=$(freechains --host=localhost:8331 chain '#Algebra' post --sign=$priKey2 file 'q_u2.pdf');
freechains --host=localhost:8331 chain '#Algebra' like $POST_U1 --sign=$priKey2

#HOST 3 (8332)
freechains --host=localhost:8332 peer localhost:8330 recv '#Algebra'
freechains --host=localhost:8332 peer localhost:8331 recv '#Algebra'
POST_U3=$(freechains --host=localhost:8332 chain '#Algebra' post --sign=$priKey3 file 'troll_u3.pdf');


#HOST 1 (8330)
freechains --host=localhost:8330 peer localhost:8331 recv '#Algebra'
freechains --host=localhost:8330 peer localhost:8332 recv '#Algebra'
freechains chain '#Algebra' like $POST_U2 --sign=$priKey

freechains chain '#Algebra' reps $pubKey
freechains chain '#Algebra' reps $pubKey2
freechains chain '#Algebra' reps $pubKey3

#...

#DIA 89 -----------------------------------------------------------------------

#USER 3 publica post valido

#HOST 1 (8330)
freechains-host now '2022-01-31 19:00:00.000'

#HOST 2 (8331)
freechains-host --port=8331 now '2022-01-31 19:05:00.000'

#HOST 3 (8332)
freechains-host --port=8332 now '2022-01-31 19:10:00.000'

#HOST 1 (8330)
freechains --host=localhost:8330 peer localhost:8331 recv '#Algebra'
freechains --host=localhost:8330 peer localhost:8332 recv '#Algebra'
POST_U1=$(freechains chain '#Algebra' post --sign=$priKey file 'q_u1.pdf');

#HOST 2 (8331)
freechains --host=localhost:8331 peer localhost:8330 recv '#Algebra'
freechains --host=localhost:8331 peer localhost:8332 recv '#Algebra'
POST_U2=$(freechains --host=localhost:8331 chain '#Algebra' post --sign=$priKey2 file 'q_u2.pdf');
freechains --host=localhost:8331 chain '#Algebra' like $POST_U1 --sign=$priKey2

#HOST 3 (8332)
freechains --host=localhost:8332 peer localhost:8330 recv '#Algebra'
freechains --host=localhost:8332 peer localhost:8331 recv '#Algebra'
POST_U3=$(freechains --host=localhost:8332 chain '#Algebra' post --sign=$priKey3 file 'q_u3.pdf');

#HOST 1 (8330)
freechains --host=localhost:8330 peer localhost:8331 recv '#Algebra'
freechains --host=localhost:8330 peer localhost:8332 recv '#Algebra'
freechains chain '#Algebra' like $POST_U2 --sign=$priKey
freechains chain '#Algebra' like $POST_U3 --sign=$priKey

freechains chain '#Algebra' reps $pubKey
freechains chain '#Algebra' reps $pubKey2
freechains chain '#Algebra' reps $pubKey3

#DIA 90 -----------------------------------------------------------------------

#HOST 1 (8330)
freechains-host now '2022-02-01 19:00:00.000'

#HOST 2 (8331)
freechains-host --port=8331 now '2022-02-01 19:05:00.000'

#HOST 3 (8332)
freechains-host --port=8332 now '2022-02-01 19:10:00.000'

#HOST 1 (8330)
freechains --host=localhost:8330 peer localhost:8331 recv '#Algebra'
freechains --host=localhost:8330 peer localhost:8332 recv '#Algebra'
POST_U1=$(freechains chain '#Algebra' post --sign=$priKey file 'q_u1.pdf');

#HOST 2 (8331)
freechains --host=localhost:8331 peer localhost:8330 recv '#Algebra'
freechains --host=localhost:8331 peer localhost:8332 recv '#Algebra'
POST_U2=$(freechains --host=localhost:8331 chain '#Algebra' post --sign=$priKey2 file 'q_u2.pdf');
freechains --host=localhost:8331 chain '#Algebra' like $POST_U1 --sign=$priKey2

#HOST 3 (8332)
freechains --host=localhost:8332 peer localhost:8330 recv '#Algebra'
freechains --host=localhost:8332 peer localhost:8331 recv '#Algebra'
POST_U3=$(freechains --host=localhost:8332 chain '#Algebra' post --sign=$priKey3 file 'q_u3.pdf');
freechains --host=localhost:8332 chain '#Algebra' like $POST_U1 --sign=$priKey3

#HOST 1 (8330)
freechains --host=localhost:8330 peer localhost:8331 recv '#Algebra'
freechains --host=localhost:8330 peer localhost:8332 recv '#Algebra'
freechains chain '#Algebra' like $POST_U2 --sign=$priKey
freechains chain '#Algebra' like $POST_U3 --sign=$priKey

freechains chain '#Algebra' reps $pubKey
freechains chain '#Algebra' reps $pubKey2
freechains chain '#Algebra' reps $pubKey3
