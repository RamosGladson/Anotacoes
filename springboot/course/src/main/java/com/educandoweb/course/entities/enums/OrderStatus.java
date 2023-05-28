package com.educandoweb.course.entities.enums;

import lombok.AllArgsConstructor;
import lombok.Getter;

@AllArgsConstructor
@Getter
public enum OrderStatus {
    WAITING_PAYMENT(1),
    PAID(2),
    SHIPPED(3),
    DELIVERED(4),
    CANCELED(5);

    private int code;

    public static OrderStatus valueOf(int code) {
        for (OrderStatus order : OrderStatus.values()) {
            if (order.getCode() == code) {
                return order;
            }
        }
        throw new IllegalArgumentException("Order status code not valid");

    }

}
