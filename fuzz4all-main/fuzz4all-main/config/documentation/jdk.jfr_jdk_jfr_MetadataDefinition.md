# Annotation Type MetadataDefinition

**Source:** `jdk.jfr\jdk\jfr\MetadataDefinition.html`

### Class Description

```java
@Retention
(
RUNTIME
)

@Target
(
TYPE
)
public @interface
MetadataDefinition
```

Meta annotation for defining new types of event metadata.

In the following example, a transaction event is defined with two
user-defined annotations,

@Severity

and

@TransactionId

.

```java
@MetadataDefinition
@Label("Severity")
@Description("Value between 0 and 100 that indicates severity. 100 is most severe.")
@Retention(RetentionPolicy.RUNTIME)
@Target({ ElementType.TYPE })
public @interface @Severity {
int value() default 50;
}

@MetadataDefinition
@Label("Transaction Id")
@Relational
@Retention(RetentionPolicy.RUNTIME)
@Target({ ElementType.FIELD })
public @interface @Severity {
}

@Severity(80)
@Label("Transaction Blocked");
class TransactionBlocked extends Event {
@TransactionId
@Label("Transaction");
long transactionId;

@TransactionId
@Label("Transaction Blocker");
long transactionId;
}
```

Adding

@MetadataDefinition

to the declaration of

@Severity

and

@TransactionId

ensures the information is saved by Flight Recorder.

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

*No entries found.*

### Additional Sections

#### Annotation Type MetadataDefinition

```java
@Retention
(
RUNTIME
)

@Target
(
TYPE
)
public @interface
MetadataDefinition
```

Meta annotation for defining new types of event metadata.

In the following example, a transaction event is defined with two
user-defined annotations,

@Severity

and

@TransactionId

.

```java
@MetadataDefinition
@Label("Severity")
@Description("Value between 0 and 100 that indicates severity. 100 is most severe.")
@Retention(RetentionPolicy.RUNTIME)
@Target({ ElementType.TYPE })
public @interface @Severity {
int value() default 50;
}

@MetadataDefinition
@Label("Transaction Id")
@Relational
@Retention(RetentionPolicy.RUNTIME)
@Target({ ElementType.FIELD })
public @interface @Severity {
}

@Severity(80)
@Label("Transaction Blocked");
class TransactionBlocked extends Event {
@TransactionId
@Label("Transaction");
long transactionId;

@TransactionId
@Label("Transaction Blocker");
long transactionId;
}
```

Adding

@MetadataDefinition

to the declaration of

@Severity

and

@TransactionId

ensures the information is saved by Flight Recorder.

**Since:** 9

@Retention

(

RUNTIME

)

@Target

(

TYPE

)
public @interface

MetadataDefinition

Meta annotation for defining new types of event metadata.

In the following example, a transaction event is defined with two
user-defined annotations,

@Severity

and

@TransactionId

.

```java
@MetadataDefinition
@Label("Severity")
@Description("Value between 0 and 100 that indicates severity. 100 is most severe.")
@Retention(RetentionPolicy.RUNTIME)
@Target({ ElementType.TYPE })
public @interface @Severity {
int value() default 50;
}

@MetadataDefinition
@Label("Transaction Id")
@Relational
@Retention(RetentionPolicy.RUNTIME)
@Target({ ElementType.FIELD })
public @interface @Severity {
}

@Severity(80)
@Label("Transaction Blocked");
class TransactionBlocked extends Event {
@TransactionId
@Label("Transaction");
long transactionId;

@TransactionId
@Label("Transaction Blocker");
long transactionId;
}
```

Adding

@MetadataDefinition

to the declaration of

@Severity

and

@TransactionId

ensures the information is saved by Flight Recorder.

In the following example, a transaction event is defined with two
user-defined annotations,

@Severity

and

@TransactionId

.

```java
@MetadataDefinition
@Label("Severity")
@Description("Value between 0 and 100 that indicates severity. 100 is most severe.")
@Retention(RetentionPolicy.RUNTIME)
@Target({ ElementType.TYPE })
public @interface @Severity {
int value() default 50;
}

@MetadataDefinition
@Label("Transaction Id")
@Relational
@Retention(RetentionPolicy.RUNTIME)
@Target({ ElementType.FIELD })
public @interface @Severity {
}

@Severity(80)
@Label("Transaction Blocked");
class TransactionBlocked extends Event {
@TransactionId
@Label("Transaction");
long transactionId;

@TransactionId
@Label("Transaction Blocker");
long transactionId;
}
```

Adding

@MetadataDefinition

to the declaration of

@Severity

and

@TransactionId

ensures the information is saved by Flight Recorder.

@MetadataDefinition
@Label("Severity")
@Description("Value between 0 and 100 that indicates severity. 100 is most severe.")
@Retention(RetentionPolicy.RUNTIME)
@Target({ ElementType.TYPE })
public @interface @Severity {
int value() default 50;
}

@MetadataDefinition
@Label("Transaction Id")
@Relational
@Retention(RetentionPolicy.RUNTIME)
@Target({ ElementType.FIELD })
public @interface @Severity {
}

@Severity(80)
@Label("Transaction Blocked");
class TransactionBlocked extends Event {
@TransactionId
@Label("Transaction");
long transactionId;

@TransactionId
@Label("Transaction Blocker");
long transactionId;
}

---

