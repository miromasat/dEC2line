THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


Description:dEC2line is a python tool allowing to gather and bring attention to groups of EC2 instances that may be active and under/over the desired utilization. The tool then populates SQS queue and optionally sends an email/text to interested parties. Code largely based on prior work at: awslabs/cost-optimization-ec2-right-sizing

Stage: Work in progress

Usage: Deploy as a cron enabled job onto EC2 instance, or deploy using cloudformation template.


Synopsis: 
```python
    import lib.index as i
    
    
    i.account_number    = os.environ['sqs_cleanup'] #account number of instance inspection, default is the account derived from EC2/Lambda running the code
    i.region_name       = os.environ['region_name'] #aws region name, e.g.: 'us-east-one'
    i.tag_name          = os.environ['tag_name'] #tag name required on instance inspection
    i.tag_value         = os.environ['tag_value'] #tag value required on instance inspection
    i.instance_type     = os.environ['instance_type'] #type of instance inspection, e.g.: 'c5d.3xlarge'
    i.instance_arn      = os.environ['instance_arn'] #instance arn
    i.vpc_arn           = os.environ['vpc_arn'] #vpc arn
    i.subnet_arn        = os.environ['subnet_arn'] #subnet arn
    i.sns_email         = os.environ['sns_email'] #notification email
    i.sns_number        = os.environ['sns_number'] #notification phone number
    i.cpu_threshold     = os.environ['cpu_threshold'] #cpu treshold period in %
    i.moreless          = os.environ['moreless'] #condition of notification triggered, a.k.a more or less of CPU to be alerted on
    i.sqs_arn           = os.environ['moreless'] #sqs arn
    i.sqs_lenght        = os.environ['sqs_lenght'] #sqs max lenghth before the warning notification sent
    i.sqs_cleanup       = os.environ['sqs_cleanup'] #sqs setting to clean the queue after the notification 
    
    i.run()
```
 