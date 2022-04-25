package midterm;

import java.io.IOException;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapred.*;

public class CountEmbarkedMapper extends MapReduceBase implements Mapper<LongWritable, Text, Text, IntWritable> {
	private final static IntWritable one = new IntWritable(1);
	private Text embarked_code = new Text();

	public void map(LongWritable key, Text value, OutputCollector<Text, IntWritable> output, Reporter reporter)
			throws IOException {

		try {
			String line = value.toString();
			String[] res = line.split(",");
			
			embarked_code.set(res[11]);
			output.collect(embarked_code, one);
		} catch(Exception e) {
			
		}
	}
}
