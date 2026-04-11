# Annotation Type ConstructorParameters

**Source:** `java.management\javax\management\ConstructorParameters.html`

### Class Description

```java
@Documented

@Target
(
CONSTRUCTOR
)

@Retention
(
RUNTIME
)
public @interface
ConstructorParameters
```

An annotation on a constructor that shows how the parameters of
that constructor correspond to the constructed object's getter
methods. For example:

```java
public class MemoryUsage {
// standard JavaBean conventions with getters

@ConstructorParameters({"init", "used", "committed", "max"})

public MemoryUsage(long init, long used,
long committed, long max) {...}
public long getInit() {...}
public long getUsed() {...}
public long getCommitted() {...}
public long getMax() {...}
}
```

The annotation shows that the first parameter of the constructor
can be retrieved with the

getInit()

method, the second one with
the

getUsed()

method, and so on. Since parameter names are not in
general available at runtime, without the annotation there would be
no way of knowing which parameter corresponds to which property.

If a constructor is annotated by the both

@java.beans.ConstructorProperties

and

@javax.management.ConstructorParameters

annotations
the JMX introspection will give an absolute precedence to the latter one.

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### value

String [] The getter names.

---

### Additional Sections

#### Annotation Type ConstructorParameters

```java
@Documented

@Target
(
CONSTRUCTOR
)

@Retention
(
RUNTIME
)
public @interface
ConstructorParameters
```

An annotation on a constructor that shows how the parameters of
that constructor correspond to the constructed object's getter
methods. For example:

```java
public class MemoryUsage {
// standard JavaBean conventions with getters

@ConstructorParameters({"init", "used", "committed", "max"})

public MemoryUsage(long init, long used,
long committed, long max) {...}
public long getInit() {...}
public long getUsed() {...}
public long getCommitted() {...}
public long getMax() {...}
}
```

The annotation shows that the first parameter of the constructor
can be retrieved with the

getInit()

method, the second one with
the

getUsed()

method, and so on. Since parameter names are not in
general available at runtime, without the annotation there would be
no way of knowing which parameter corresponds to which property.

If a constructor is annotated by the both

@java.beans.ConstructorProperties

and

@javax.management.ConstructorParameters

annotations
the JMX introspection will give an absolute precedence to the latter one.

**Since:** 9

@Documented

@Target

(

CONSTRUCTOR

)

@Retention

(

RUNTIME

)
public @interface

ConstructorParameters

An annotation on a constructor that shows how the parameters of
that constructor correspond to the constructed object's getter
methods. For example:

```java
public class MemoryUsage {
// standard JavaBean conventions with getters

@ConstructorParameters({"init", "used", "committed", "max"})

public MemoryUsage(long init, long used,
long committed, long max) {...}
public long getInit() {...}
public long getUsed() {...}
public long getCommitted() {...}
public long getMax() {...}
}
```

The annotation shows that the first parameter of the constructor
can be retrieved with the

getInit()

method, the second one with
the

getUsed()

method, and so on. Since parameter names are not in
general available at runtime, without the annotation there would be
no way of knowing which parameter corresponds to which property.

If a constructor is annotated by the both

@java.beans.ConstructorProperties

and

@javax.management.ConstructorParameters

annotations
the JMX introspection will give an absolute precedence to the latter one.

An annotation on a constructor that shows how the parameters of
that constructor correspond to the constructed object's getter
methods. For example:

public class MemoryUsage {
// standard JavaBean conventions with getters

@ConstructorParameters({"init", "used", "committed", "max"})

public MemoryUsage(long init, long used,
long committed, long max) {...}
public long getInit() {...}
public long getUsed() {...}
public long getCommitted() {...}
public long getMax() {...}
}

The annotation shows that the first parameter of the constructor
can be retrieved with the

getInit()

method, the second one with
the

getUsed()

method, and so on. Since parameter names are not in
general available at runtime, without the annotation there would be
no way of knowing which parameter corresponds to which property.

If a constructor is annotated by the both

@java.beans.ConstructorProperties

and

@javax.management.ConstructorParameters

annotations
the JMX introspection will give an absolute precedence to the latter one.

=========== ANNOTATION TYPE REQUIRED MEMBER SUMMARY ===========

- Required Element Summary

Required Elements

Modifier and Type

Required Element

Description

String

[]

value

The getter names.

Required Element Summary

Required Elements

Modifier and Type

Required Element

Description

String

[]

value

The getter names.

---

#### Required Element Summary

The getter names.

============ ANNOTATION TYPE MEMBER DETAIL ===========

- Element Detail

- value

```java
String
[] value
```

The getter names.

**Returns:** the getter names corresponding to the parameters in the
annotated constructor.

Element Detail

- value

```java
String
[] value
```

The getter names.

**Returns:** the getter names corresponding to the parameters in the
annotated constructor.

---

#### Element Detail

value

```java
String
[] value
```

The getter names.

**Returns:** the getter names corresponding to the parameters in the
annotated constructor.

---

#### value

String

[] value

The getter names.

---

