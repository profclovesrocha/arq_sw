package com.pay.payment_api.event;

import lombok.*;

import java.io.Serializable;
import java.math.BigDecimal;
import java.util.UUID;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class OrderCreatedEvent implements Serializable {

    private UUID orderId;

    private UUID customerId;

    private BigDecimal amount;
}
