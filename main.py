import beanstalk as b
import file_helper as h

if __name__ == '__main__':
    host = "192.168.99.69"
    tube = "sc_instagram_post_comment_beta"
    lines = h.read_file('sample_text.txt')

    # Open connection beanstalk
    beans = b.Beanstalk(host=host, tube=tube)

    # Push job to beanstalk
    for line in lines:
        # data = {
        #     "code": line
        # }

        data = {
            "code": line
            # "keyword": line,
            # "since": "2021-06-21"
            #
            # "id": line
        }
        job = h.formatted_dict(data)
        beans.push(body=job)

    # Close Beanstalk connection
    beans.close()
