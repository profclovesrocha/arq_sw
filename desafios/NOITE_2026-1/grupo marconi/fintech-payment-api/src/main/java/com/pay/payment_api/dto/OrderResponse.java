package com.pay.payment_api.dto;

import java.math.BigDecimal;
import java.time.LocalDateTime;
import java.util.UUID;

public record OrderResponse(
        UUID id,
        UUID customerId,
        BigDecimal amount,
        String status,
        LocalDateTime createdAt
){}
