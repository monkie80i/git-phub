# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testanswer',
            name='a1',
            field=models.CharField(max_length=1, choices=[(b'a', b'Interact with many, including strangers'), (b'b', b'Interact with a few, known to you')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a10',
            field=models.CharField(max_length=1, choices=[(b'a', b'What is actual'), (b'b', b'What is possible')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a11',
            field=models.CharField(max_length=1, choices=[(b'a', b'Laws than circumstances'), (b'b', b'Circumstances than laws')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a12',
            field=models.CharField(max_length=1, choices=[(b'a', b'Objective'), (b'b', b'Personal')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a13',
            field=models.CharField(max_length=1, choices=[(b'a', b'Punctual'), (b'b', b'Leisurely')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a14',
            field=models.CharField(max_length=1, choices=[(b'a', b'Incomplete'), (b'b', b'Completed')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a15',
            field=models.CharField(max_length=1, choices=[(b'a', b"Keep abreast of other's happenings"), (b'b', b'Get behind on the news')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a16',
            field=models.CharField(max_length=1, choices=[(b'a', b'Do it the usual way'), (b'b', b'Do it your o')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a17',
            field=models.CharField(max_length=1, choices=[(b'a', b'Say what they mean and mean what they say'), (b'b', b'Express things more by use of analogy')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a18',
            field=models.CharField(max_length=1, choices=[(b'a', b'Consistency of thought'), (b'b', b'Harmonious human relationships')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a19',
            field=models.CharField(max_length=1, choices=[(b'a', b'Logical judgments'), (b'b', b'Value judgments')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a2',
            field=models.CharField(max_length=1, choices=[(b'a', b'Realistic than speculative'), (b'b', b'Speculative than realistic')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a20',
            field=models.CharField(max_length=1, choices=[(b'a', b'Settled and decided'), (b'b', b'Unsettled and undecided')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a21',
            field=models.CharField(max_length=1, choices=[(b'a', b'Serious and determined'), (b'b', b'Easy-going')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a22',
            field=models.CharField(max_length=1, choices=[(b'a', b'Rarely question that it will all be said'), (b'b', b"Rehearse what you'll say")]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a23',
            field=models.CharField(max_length=1, choices=[(b'a', b'"Speak for themselves"'), (b'b', b'Illustrate principles')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a24',
            field=models.CharField(max_length=1, choices=[(b'a', b'somewhat annoying'), (b'b', b'rather fascinating')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a25',
            field=models.CharField(max_length=1, choices=[(b'a', b'a cool-headed person'), (b'b', b'a warm-hearted person')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a26',
            field=models.CharField(max_length=1, choices=[(b'a', b'unjust'), (b'b', b'merciless')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a27',
            field=models.CharField(max_length=1, choices=[(b'a', b'by careful selection and choice'), (b'b', b'randomly and by chance')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a28',
            field=models.CharField(max_length=1, choices=[(b'a', b' having purchased'), (b'b', b'having the option to buy')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a29',
            field=models.CharField(max_length=1, choices=[(b'a', b'initiate conversation'), (b'b', b'wait to be approached')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a3',
            field=models.CharField(max_length=1, choices=[(b'a', b'Have your "head in the clouds"'), (b'b', b'Be "in a rut"')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a30',
            field=models.CharField(max_length=1, choices=[(b'a', b'rarely questionable'), (b'b', b'frequently questionable')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a31',
            field=models.CharField(max_length=1, choices=[(b'a', b'make themselves useful enough'), (b'b', b'exercise their fantasy enough')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a32',
            field=models.CharField(max_length=1, choices=[(b'a', b'standards'), (b'b', b'feelings')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a33',
            field=models.CharField(max_length=1, choices=[(b'a', b'firm than gentle'), (b'b', b'gentle than firm')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a34',
            field=models.CharField(max_length=1, choices=[(b'a', b'the ability to organize and be methodical'), (b'b', b'the ability to adapt and make do')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a35',
            field=models.CharField(max_length=1, choices=[(b'a', b'infinite'), (b'b', b'open-minded')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a36',
            field=models.CharField(max_length=1, choices=[(b'a', b'stimulate and energize you'), (b'b', b'tax your reserves')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a37',
            field=models.CharField(max_length=1, choices=[(b'a', b'a practical sort of person'), (b'b', b'a fanciful sort of person')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a38',
            field=models.CharField(max_length=1, choices=[(b'a', b'see how others are useful'), (b'b', b'see how others see')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a39',
            field=models.CharField(max_length=1, choices=[(b'a', b'to discuss an issue thoroughly'), (b'b', b'to arrive at agreement on an issue')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a4',
            field=models.CharField(max_length=1, choices=[(b'a', b'Principles'), (b'b', b'Emotions')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a40',
            field=models.CharField(max_length=1, choices=[(b'a', b'your head'), (b'b', b'your heart')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a41',
            field=models.CharField(max_length=1, choices=[(b'a', b'contracted'), (b'b', b'done on a casual basis')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a42',
            field=models.CharField(max_length=1, choices=[(b'a', b'the orderly'), (b'b', b'whatever turns up')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a43',
            field=models.CharField(max_length=1, choices=[(b'a', b'many friends with brief contact'), (b'b', b'a few friends with more lengthy contact')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a44',
            field=models.CharField(max_length=1, choices=[(b'a', b'facts'), (b'b', b'principles')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a45',
            field=models.CharField(max_length=1, choices=[(b'a', b'production and distribution'), (b'b', b'design and research')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a46',
            field=models.CharField(max_length=1, choices=[(b'a', b'"There is a very logical person."'), (b'b', b'"There is a very sentimental person."')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a47',
            field=models.CharField(max_length=1, choices=[(b'a', b'unwavering'), (b'b', b'devoted')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a48',
            field=models.CharField(max_length=1, choices=[(b'a', b'final and unalterable statement'), (b'b', b'tentative and preliminary statement')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a49',
            field=models.CharField(max_length=1, choices=[(b'a', b'after a decision'), (b'b', b'before a decision')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a5',
            field=models.CharField(max_length=1, choices=[(b'a', b'Convincing'), (b'b', b'Touching')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a50',
            field=models.CharField(max_length=1, choices=[(b'a', b'speak easily and at length with strangers'), (b'b', b'find little to say to strangers')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a51',
            field=models.CharField(max_length=1, choices=[(b'a', b'experience'), (b'b', b'hunch')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a52',
            field=models.CharField(max_length=1, choices=[(b'a', b'more practical than ingenious'), (b'b', b'more ingenious than practical')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a53',
            field=models.CharField(max_length=1, choices=[(b'a', b'clear reason'), (b'b', b'strong feeling')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a54',
            field=models.CharField(max_length=1, choices=[(b'a', b'fair-minded'), (b'b', b'sympathetic')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a55',
            field=models.CharField(max_length=1, choices=[(b'a', b'make sure things are arranged'), (b'b', b'just let things happen')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a56',
            field=models.CharField(max_length=1, choices=[(b'a', b're-negotiable'), (b'b', b'random and circumstantial')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a57',
            field=models.CharField(max_length=1, choices=[(b'a', b'hasten to get to it first'), (b'b', b'hope someone else will answer')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a58',
            field=models.CharField(max_length=1, choices=[(b'a', b'a strong sense of reality'), (b'b', b'a vivid imagination')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a59',
            field=models.CharField(max_length=1, choices=[(b'a', b'fundamentals'), (b'b', b'overtones')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a6',
            field=models.CharField(max_length=1, choices=[(b'a', b'To deadlines'), (b'b', b'Just "whenever"')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a60',
            field=models.CharField(max_length=1, choices=[(b'a', b'to be too passionate'), (b'b', b'to be too objective')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a61',
            field=models.CharField(max_length=1, choices=[(b'a', b'hard-headed'), (b'b', b'soft-hearted')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a62',
            field=models.CharField(max_length=1, choices=[(b'a', b'the structured and scheduled'), (b'b', b'the unstructured and unscheduled')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a63',
            field=models.CharField(max_length=1, choices=[(b'a', b'routinized than whimsical'), (b'b', b'whimsical than routinized')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a64',
            field=models.CharField(max_length=1, choices=[(b'a', b'easy to approach'), (b'b', b'somewhat reserved')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a65',
            field=models.CharField(max_length=1, choices=[(b'a', b'the more literal'), (b'b', b'the more figurative')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a66',
            field=models.CharField(max_length=1, choices=[(b'a', b'identify with others'), (b'b', b'utilize others')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a67',
            field=models.CharField(max_length=1, choices=[(b'a', b'clarity of reason'), (b'b', b'strength of compassion')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a68',
            field=models.CharField(max_length=1, choices=[(b'a', b'being indiscriminate'), (b'b', b'being critical')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a69',
            field=models.CharField(max_length=1, choices=[(b'a', b'planned event'), (b'b', b'unplanned event')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a7',
            field=models.CharField(max_length=1, choices=[(b'a', b'Rather carefully'), (b'b', b'Somewhat impulsively')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a70',
            field=models.CharField(max_length=1, choices=[(b'a', b'deliberate than spontaneous'), (b'b', b'spontaneous than deliberate')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a8',
            field=models.CharField(max_length=1, choices=[(b'a', b'Stay late, with increasing energy'), (b'b', b'Leave early with decreased energy')]),
        ),
        migrations.AlterField(
            model_name='testanswer',
            name='a9',
            field=models.CharField(max_length=1, choices=[(b'a', b'Sensible people'), (b'b', b'Imaginative people')]),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='abbrev',
            field=models.CharField(max_length=4),
        ),
    ]
