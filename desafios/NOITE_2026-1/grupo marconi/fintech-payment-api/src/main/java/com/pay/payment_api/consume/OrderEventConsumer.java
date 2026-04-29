package com.pay.payment_api.consume;

import com.pay.payment_api.config.RabbitMQConfig;
import com.pay.payment_api.event.OrderCreatedEvent;
import lombok.extern.slf4j.Slf4j;
import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.stereotype.Component;

@Component
@Slf4j
public class OrderEventConsumer {

    @RabbitListener(queues = RabbitMQConfig.QUEUE)
    public void consume(OrderCreatedEvent event){

        log.info("Evento recebido do RabbitMQ: {}", event);
    }
}
