package designmode.facade;

/*门面模式： 外部与一个子系统的通信必须通过一个统一的门面（Facade）对象来进行
 * 1. 举例：
 * 		医院（子系统角色）： 挂号，门诊，划价，化验，收费，取药各个子系统
 * 		病人： 需要和医院的各个子系统打交道
 * 		门面（门面角色）：相当于接待员，病人和接待员打交道，接待员和医院内部各个子系统通信
 * 
 * 2. 使用
 * 	（1）为一个复杂的系统提供一个简单的接口
 * 	（2）提高子系统的独立性
 * 
 */
public class Facade {
	private ICook icook;
	private IWaiter iwaiter;
	private IPayment ipay;
	
	public Facade() {
		ipay = new PaymentImp();
		icook = new CookImp();
		iwaiter = new WaiterImp();
	}
	
	public void serve() {
		String food = ipay.pay();
		food = icook.cook(food);
		iwaiter.serve(food);
	}
}
