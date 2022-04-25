package midterm;

import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapred.*;

public class CountEmbarkedMain {

	public static void main(String[] args) throws Exception {
		JobConf conf = new JobConf(CountEmbarkedMain.class);
		conf.setJobName("titanic");

		conf.setOutputKeyClass(Text.class);
		conf.setOutputValueClass(IntWritable.class);

		conf.setMapperClass(CountEmbarkedMapper.class);
		conf.setCombinerClass(CountEmbarkedReducer.class);
		conf.setReducerClass(CountEmbarkedReducer.class);

		conf.setInputFormat(TextInputFormat.class);
		conf.setOutputFormat(TextOutputFormat.class);

		FileInputFormat.setInputPaths(conf, new Path(args[0]));
		FileOutputFormat.setOutputPath(conf, new Path(args[1]));
		JobClient.runJob(conf);
	}

}
