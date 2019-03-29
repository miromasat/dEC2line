THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Description:dEC2line is a python tool allowing to gather and bring attention to groups of EC2 instances that may be active and under/over the desired utilization. The tool then populates SQS queue and optionally sends an email/text to interested parties. Code largely based on prior work at: awslabs/cost-optimization-ec2-right-sizing
Stage: Work in progress
Usage: Deploy as a cron enabled job onto EC2 instance, or deploy using cloudformation template.

