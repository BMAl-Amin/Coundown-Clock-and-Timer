import sys
import time


class CountDown:

    import time
    def countdown_time(self, time_length):
        """
     :param time_length:
     This method divide seconds into minutes and start countdown
        """
        print(f'Your countdown length is {time_length} minutes')
        seconds_length = int(time_length) * 60
        while seconds_length:
            mins, secs = divmod(seconds_length, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            sys.stdout.write("\r%s" % timer)
            sys.stdout.flush()
            time.sleep(1)
            seconds_length -= 1

        print(' STOP!')
