package com.pay.payment_api.config;

import org.springframework.amqp.core.Binding;
import org.springframework.amqp.core.BindingBuilder;
import org.springframework.amqp.core.TopicExchange;
import org.springframework.amqp.rabbit.connection.ConnectionFactory;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.amqp.support.converter.Jackson2JsonMessageConverter;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import org.springframework.amqp.core.Queue;

import java.util.HashMap;
import java.util.Map;

@Configuration
public class RabbitMQConfig {

    public static final String QUEUE = "payment.queue";

    public static final String EXCHANGE = "payment.exchange";

    public static final String ROUNTING_KEY = "payment.created";

    public static final String DLQ = "payment.dlq";

    public static final String DLX = "payment.dlx";

    @Bean
    public Queue queue() {

        Map<String, Object> args = new HashMap<>();

        args.put("x-dead-letter-exchange", DLX);
        args.put("x-dead-letter-routing-key", ROUNTING_KEY);

        return new Queue(QUEUE, true, false, false, args);
    }

    @Bean
    public TopicExchange exchange(){
        return new TopicExchange(EXCHANGE);
    }

    @Bean
    public Queue deadLetterQueue(){
        return new Queue(DLQ);
    }

    @Bean
    public TopicExchange deadLetterExchange(){
        return new TopicExchange(DLX);
    }
    @Bean
    public Jackson2JsonMessageConverter messageConverter(){
        return new Jackson2JsonMessageConverter();
    }

    @Bean
    public RabbitTemplate rabbitTemplate(ConnectionFactory connectionFactory){
        RabbitTemplate template = new RabbitTemplate(connectionFactory);
        template.setMessageConverter(messageConverter());
        return template;
    }

    @Bean
    public Binding binding(Queue queue, TopicExchange exchange){
        return BindingBuilder.bind(queue).to(exchange).with(ROUNTING_KEY);
    }
}
