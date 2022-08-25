## 1. playlist_track 테이블에 `A`라는 별칭을 부여하고 데이터를 출력하세요.

| 단, 모든 컬럼을 `PlaylistId` 기준으로 내림차순으로 5개만 출력하세요.

```sql
select * from playlist_track AS A 
order by A.playlistid desc limit 5;
```

### 2. tracks 테이블에 `B`라는 별칭을 부여하고 데이터를 출력하세요

| 단, 모든 컬럼을 `TrackId` 기준으로 오름차순으로 5개만 출력하세요.

```sql
select * from tracks AS B
order by B.trackid limit 5;
```

### 3. 각 playlist_track 해당하는 track 데이터를 함께 출력하세요.

| 단, PlaylistId, Name 컬럼을 `PlaylistId` 기준으로 내림차순으로 10개만 출력하세요. 

```sql
select A.playlistid,B.name from playlist_track AS A inner join tracks AS B
on A.trackid = B.trackid
order by playlistid desc limit 10;
```

### 4. `PlaylistId`가 `10`인 track 데이터를 함께 출력하세요.

| 단, PlaylistId, Name 컬럼을 `Name` 기준으로 내림차순으로 5개만 출력하세요.

```sql
select playlistid,name from playlist_track inner join tracks
on playlist_track.trackid = tracks.trackid where playlistid = 10
order by name DESC
limit 5;
```

### 5. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `INNER JOIN`해서 데이터를 출력하세요.

| 단, 행의 개수만 출력하세요.

```sql
select count(*) from tracks A
inner join artists B
on A.composer = B.name;
```

### 6. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `LEFT JOIN`해서 데이터를 출력하세요.

| 단, 행의 개수만 출력하세요.

```sql
select count(*) from tracks A
left join artists B
on A.composer = B.name;
```

### 7. `INNER JOIN` 과 `LEFT JOIN` 행의 개수가 다른 이유를 작성하세요.

```plain
inner join 은 주어진 조건 하에 A 와 B의 교집합 부분에 해당하고
left join  은 주어진 조건 하에 A 와 B의 집합 중 A집합 부분에 해당하기 때문이다.inner join 은 주어진 조건 하에 A와 
```

### 8. invoice_items 테이블의 데이터를 출력하세요.

| 단, InvoiceLineId, InvoiceId 컬럼을 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.

```sql
select invoicelineid,invoiceid from invoice_items
order by invoiceid asc limit 5;
```

### 9. invoices 테이블의 데이터를 출력하세요.

| 단, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.

```sql
select invoiceid,customerid from invoices
order by invoiceid asc limit 5;
```

### 10. 각 invoices_item에 해당하는 invoice 데이터를 함께 출력하세요.

| 단, InvoiceLineId, InvoiceId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.

```
select A.invoicelineid,B.invoiceid from invoice_items A
inner join invoices B
on A.invoiceid = B.invoiceid
order by B.invoiceid DESC limit 5;
```

### 11. 각 invoice에 해당하는 customer 데이터를 함께 출력하세요.

| 단, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.

```
select A.invoiceid, B.customerid from invoices A
inner join customers B
on A.customerid = B.customerid
order by A.invoiceid desc limit 5;
```

### 12. 각 invoices_item(상품)을 포함하는 invoice(송장)와 해당 invoice를 받을 customer(고객) 데이터를 모두 함께 출력하세요.

| 단, InvoiceLineId, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.

```

```

### 13. 각 cusotmer가 주문한 invoices_item의 개수를 출력하세요.

| 단, CustomerId와 개수 컬럼을 `CustomerId` 기준으로 오름차순으로 5개만 출력하세요.

```sql

```
