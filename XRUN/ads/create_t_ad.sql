create table t_ad -- temporary name
(
    transaction     int auto_increment primary key,
    action          int       default 3300              not null comment '거래항목',
    currency        int                                 null comment '화폐명',
    amount          decimal(40, 25)                     null comment '금액',
    amountasxrun    decimal(40, 25)                     null comment 'xrun환산금액',
    xrun            decimal(40, 25)                     null comment 'xrun회사분',
    coinowner       decimal(40, 25)                     null comment '암호화폐사분',
    datetime        timestamp default CURRENT_TIMESTAMP not null comment '등록일',
    member          int                                 null comment '회원',
    admember        int                                 null comment '광고주 code',
    advertisement   int                                 null comment '광고 id',
    answer          int                                 null comment '답변',
    rct             int                                 null comment '전송코인',
    exchange        int                                 null comment '교환코인',
    status          int       default 9101              null,
    extracode       int       default 9400              null comment '기타코드',
    coin            int                                 null comment '코인번호',
    excuteddatetime datetime  default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP comment '마지막 변경시각',
    isdeleted       int       default 9401              null comment '삭제여부',
    result          int                                 null comment '광고 API 결과값',
    extrastr        varchar(45)                         null comment '광고 API 결과 메시지',
    extrastr2       varchar(124)                        null comment '광고 URL',
    extrastr3       varchar(100)                        null,
    extrastr4       varchar(20)                         null,
    lottery         int       default 0                 null comment '랜덤광고 번호',
    extracurrency   int                                 null
);

create index idxaction on Transaction (action);

create index idxmember on Transaction (member);
