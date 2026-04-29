package com.pay.payment_api.producer;

import com.pay.payment_api.config.RabbitMQConfig;
import com.pay.payment_api.event.OrderCreatedEvent;
import lombok.RequiredArgsConstructor;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.stereotype.Component;

@Component
@RequiredArgsConstructor
public class OrderEventProducer {

    private final RabbitTemplate rabbitTemplate;

    public void sendOrderCreatedEvent(OrderCreatedEvent event) {

        rabbitTemplate.convertAndSend(
                RabbitMQConfig.EXCHANGE,
                RabbitMQConfig.ROUNTING_KEY,
                event
        );

    }

}