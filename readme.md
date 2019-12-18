测试自动化框架使用说明

Framework: 测试过程中的一些公用方法可以存放这个目录，方便其它模块调用。在该目录中代码中定义了打印日志、读取yaml配置文件以、保存测试报告、截图及发送邮件的方法。

Logs :保存测试过程中生成的日志文件，日志文件名后缀为.txt，日志文件保存格式可以自己定义，比如.log。

Testcase：测试类文件，建议一个功能一个测试类，在测试类加入测试用例方法，依据功能来决定，另外这里要注意一下就是测试文件和测试用列需以test*或者以*test结尾。

testConfig:相关配置文件目录。可以把一些全局的配置，如测试地址，邮箱服务器地址等配置项，也可以把测试用例存入配置文件，建议用yaml文件格式。

testReport:测试报告存储位置，另报告的生成需要HTMLTestRunner.py支持。

runALL:运行全部测试用例,右键-run as …可以达到运行全部用例的目的。

Base：二次封装selenium的方法和待测页面的操作步骤，这里引入的是POB设计模式。

requirements.txt：此框架需要安装的第三方包。

# 什么是POM

 POM，中文字母意思是，页面对象模型，POM是一种最近几年非常流行的自动化测试模型，或者思想，POM不是一个框架，就是一个解决问题的思想。采用POM的目的，是为了解决前端中UI变化频繁，从而造成测试自动化脚本维护的成本越来越大。
[![POBcb23078f39e32d65.png](https://www.privacypic.com/images/2019/10/22/POBcb23078f39e32d65.png)](https://www.privacypic.com/image/lCbfgg)

 从上图看出，采取了POM设计思路和不采取的区别，左侧把测试代码和页面元素都写在一个类文件，如果需要更改页面，那么就要修改页面元素定位，从而要修改这个类中测试代码，这个看起来和混乱。右侧，采取POM后，主要的区别就是，把页面元素和业务逻辑和测试脚本分离出来到两个不同类文件。ClassA只写页面元素定位，和业务逻辑代码操作的封装，ClassB只写测试脚本，不关心如何元素定位，只写调用ClassA的代码去覆盖不同的测试场景。如果前端页面发生变化，只需要修改ClassA的元素定位，而不需要去修改ClassB中的测试脚本代码。

POM主要有以下优点：

1. 把web ui对象仓库从测试脚本，业务代码和测试脚本分离。

2. 每一个页面对应一个页面类，页面的元素写到这个页面类中。

3. 页面类主要包括该页面的元素定位，和这些元素相关的业务操作代码封装的方法。

4. 代码复用，从而减少测试脚本代码量。

5. 层次清晰，同时支持多个编写自动化脚本开发，例如每个人写哪几个页面，不影响他人。

6. 建议页面类和业务逻辑方法都给一个有意义的名称，方便他人快速编写脚本和维护脚本。
