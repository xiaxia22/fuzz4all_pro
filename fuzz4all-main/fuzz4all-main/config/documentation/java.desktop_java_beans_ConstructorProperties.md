# Annotation Type ConstructorProperties

**Source:** `java.desktop\java\beans\ConstructorProperties.html`

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
ConstructorProperties
```

An annotation on a constructor that shows how the parameters of
that constructor correspond to the constructed object's getter
methods. For example:

```java
public class Point {
@ConstructorProperties({"x", "y"})
public Point(int x, int y) {
this.x = x;
this.y = y;
}

public int getX() {
return x;
}

public int getY() {
return y;
}

private final int x, y;
}
```

The annotation shows that the first parameter of the constructor
can be retrieved with the

getX()

method and the second with
the

getY()

method. Since parameter names are not in
general available at runtime, without the annotation there would be
no way to know whether the parameters correspond to

getX()

and

getY()

or the other way around.

**Since:** 1.6

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

#### Annotation Type ConstructorProperties

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
ConstructorProperties
```

An annotation on a constructor that shows how the parameters of
that constructor correspond to the constructed object's getter
methods. For example:

```java
public class Point {
@ConstructorProperties({"x", "y"})
public Point(int x, int y) {
this.x = x;
this.y = y;
}

public int getX() {
return x;
}

public int getY() {
return y;
}

private final int x, y;
}
```

The annotation shows that the first parameter of the constructor
can be retrieved with the

getX()

method and the second with
the

getY()

method. Since parameter names are not in
general available at runtime, without the annotation there would be
no way to know whether the parameters correspond to

getX()

and

getY()

or the other way around.

**Since:** 1.6

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

ConstructorProperties

An annotation on a constructor that shows how the parameters of
that constructor correspond to the constructed object's getter
methods. For example:

```java
public class Point {
@ConstructorProperties({"x", "y"})
public Point(int x, int y) {
this.x = x;
this.y = y;
}

public int getX() {
return x;
}

public int getY() {
return y;
}

private final int x, y;
}
```

The annotation shows that the first parameter of the constructor
can be retrieved with the

getX()

method and the second with
the

getY()

method. Since parameter names are not in
general available at runtime, without the annotation there would be
no way to know whether the parameters correspond to

getX()

and

getY()

or the other way around.

public class Point {
@ConstructorProperties({"x", "y"})
public Point(int x, int y) {
this.x = x;
this.y = y;
}

public int getX() {
return x;
}

public int getY() {
return y;
}

private final int x, y;
}

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

