# Class Query

**Source:** `java.management\javax\management\Query.html`

### Class Description

```java
public class
Query

extends
Object
```

Constructs query object constraints.

The MBean Server can be queried for MBeans that meet a particular
condition, using its

queryNames

or

queryMBeans

method. The

QueryExp

parameter to the method can be any implementation of the interface

QueryExp

, but it is usually best to obtain the

QueryExp

value by calling the static methods in this class. This is particularly
true when querying a remote MBean Server: a custom implementation of the

QueryExp

interface might not be present in the remote MBean Server,
but the methods in this class return only standard classes that are
part of the JMX implementation.

As an example, suppose you wanted to find all MBeans where the

Enabled

attribute is

true

and the

Owner

attribute is

"Duke"

. Here is how you could construct the appropriate

QueryExp

by
chaining together method calls:

```java
QueryExp query =
Query.and(Query.eq(Query.attr("Enabled"), Query.value(true)),
Query.eq(Query.attr("Owner"), Query.value("Duke")));
```

**Since:** 1.5

---

### Field Details

#### public static final int GT

A code representing the

gt(javax.management.ValueExp, javax.management.ValueExp)

query. This is chiefly
of interest for the serialized form of queries.

**See Also:**
- Constant Field Values

---

#### public static final int LT

A code representing the

lt(javax.management.ValueExp, javax.management.ValueExp)

query. This is chiefly
of interest for the serialized form of queries.

**See Also:**
- Constant Field Values

---

#### public static final int GE

A code representing the

geq(javax.management.ValueExp, javax.management.ValueExp)

query. This is chiefly
of interest for the serialized form of queries.

**See Also:**
- Constant Field Values

---

#### public static final int LE

A code representing the

leq(javax.management.ValueExp, javax.management.ValueExp)

query. This is chiefly
of interest for the serialized form of queries.

**See Also:**
- Constant Field Values

---

#### public static final int EQ

A code representing the

eq(javax.management.ValueExp, javax.management.ValueExp)

query. This is chiefly
of interest for the serialized form of queries.

**See Also:**
- Constant Field Values

---

#### public static final int PLUS

A code representing the

plus(javax.management.ValueExp, javax.management.ValueExp)

expression. This
is chiefly of interest for the serialized form of queries.

**See Also:**
- Constant Field Values

---

#### public static final int MINUS

A code representing the

minus(javax.management.ValueExp, javax.management.ValueExp)

expression. This
is chiefly of interest for the serialized form of queries.

**See Also:**
- Constant Field Values

---

#### public static final int TIMES

A code representing the

times(javax.management.ValueExp, javax.management.ValueExp)

expression. This
is chiefly of interest for the serialized form of queries.

**See Also:**
- Constant Field Values

---

#### public static final int DIV

A code representing the

div(javax.management.ValueExp, javax.management.ValueExp)

expression. This is
chiefly of interest for the serialized form of queries.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public Query()

Basic constructor.

---

### Method Details

#### public static
QueryExp
and​(
QueryExp
q1,

QueryExp
q2)

Returns a query expression that is the conjunction of two other query
expressions.

**Parameters:**
- q1

- A query expression.
- q2

- Another query expression.

**Returns:**
- The conjunction of the two arguments. The returned object
will be serialized as an instance of the non-public class

javax.management.AndQueryExp

.

---

#### public static
QueryExp
or​(
QueryExp
q1,

QueryExp
q2)

Returns a query expression that is the disjunction of two other query
expressions.

**Parameters:**
- q1

- A query expression.
- q2

- Another query expression.

**Returns:**
- The disjunction of the two arguments. The returned object
will be serialized as an instance of the non-public class

javax.management.OrQueryExp

.

---

#### public static
QueryExp
gt​(
ValueExp
v1,

ValueExp
v2)

Returns a query expression that represents a "greater than" constraint on
two values.

**Parameters:**
- v1

- A value expression.
- v2

- Another value expression.

**Returns:**
- A "greater than" constraint on the arguments. The
returned object will be serialized as an instance of the
non-public class

javax.management.BinaryRelQueryExp

with a

relOp

equal
to

GT

.

---

#### public static
QueryExp
geq​(
ValueExp
v1,

ValueExp
v2)

Returns a query expression that represents a "greater than or equal
to" constraint on two values.

**Parameters:**
- v1

- A value expression.
- v2

- Another value expression.

**Returns:**
- A "greater than or equal to" constraint on the
arguments. The returned object will be serialized as an
instance of the non-public class

javax.management.BinaryRelQueryExp

with a

relOp

equal
to

GE

.

---

#### public static
QueryExp
leq​(
ValueExp
v1,

ValueExp
v2)

Returns a query expression that represents a "less than or equal to"
constraint on two values.

**Parameters:**
- v1

- A value expression.
- v2

- Another value expression.

**Returns:**
- A "less than or equal to" constraint on the arguments.
The returned object will be serialized as an instance of the
non-public class

javax.management.BinaryRelQueryExp

with a

relOp

equal
to

LE

.

---

#### public static
QueryExp
lt​(
ValueExp
v1,

ValueExp
v2)

Returns a query expression that represents a "less than" constraint on
two values.

**Parameters:**
- v1

- A value expression.
- v2

- Another value expression.

**Returns:**
- A "less than" constraint on the arguments. The
returned object will be serialized as an instance of the
non-public class

javax.management.BinaryRelQueryExp

with a

relOp

equal
to

LT

.

---

#### public static
QueryExp
eq​(
ValueExp
v1,

ValueExp
v2)

Returns a query expression that represents an equality constraint on
two values.

**Parameters:**
- v1

- A value expression.
- v2

- Another value expression.

**Returns:**
- A "equal to" constraint on the arguments. The
returned object will be serialized as an instance of the
non-public class

javax.management.BinaryRelQueryExp

with a

relOp

equal
to

EQ

.

---

#### public static
QueryExp
between​(
ValueExp
v1,

ValueExp
v2,

ValueExp
v3)

Returns a query expression that represents the constraint that one
value is between two other values.

**Parameters:**
- v1

- A value expression that is "between" v2 and v3.
- v2

- Value expression that represents a boundary of the constraint.
- v3

- Value expression that represents a boundary of the constraint.

**Returns:**
- The constraint that v1 lies between v2 and v3. The
returned object will be serialized as an instance of the
non-public class

javax.management.BetweenQueryExp

.

---

#### public static
QueryExp
match​(
AttributeValueExp
a,

StringValueExp
s)

Returns a query expression that represents a matching constraint on
a string argument. The matching syntax is consistent with file globbing:
supports "

?

", "

*

", "

[

",
each of which may be escaped with "

\

";
character classes may use "

!

" for negation and
"

-

" for range.
(

*

for any character sequence,

?

for a single arbitrary character,

[...]

for a character sequence).
For example:

a*b?c

would match a string starting
with the character

a

, followed
by any number of characters, followed by a

b

,
any single character, and a

c

.

**Parameters:**
- a

- An attribute expression
- s

- A string value expression representing a matching constraint

**Returns:**
- A query expression that represents the matching
constraint on the string argument. The returned object will
be serialized as an instance of the non-public class

javax.management.MatchQueryExp

.

---

#### public static
AttributeValueExp
attr​(
String
name)

Returns a new attribute expression. See

AttributeValueExp

for a detailed description of the semantics of the expression.

Evaluating this expression for a given

objectName

includes performing

MBeanServer.getAttribute(objectName,
name)

.

**Parameters:**
- name

- The name of the attribute.

**Returns:**
- An attribute expression for the attribute named

name

.

---

#### public static
AttributeValueExp
attr​(
String
className,

String
name)

Returns a new qualified attribute expression.

Evaluating this expression for a given

objectName

includes performing

MBeanServer.getObjectInstance(objectName)

and

MBeanServer.getAttribute(objectName,
name)

.

**Parameters:**
- className

- The name of the class possessing the attribute.
- name

- The name of the attribute.

**Returns:**
- An attribute expression for the attribute named name.
The returned object will be serialized as an instance of the
non-public class

javax.management.QualifiedAttributeValueExp

.

---

#### public static
AttributeValueExp
classattr()

Returns a new class attribute expression which can be used in any
Query call that expects a ValueExp.

Evaluating this expression for a given

objectName

includes performing

MBeanServer.getObjectInstance(objectName)

.

**Returns:**
- A class attribute expression. The returned object
will be serialized as an instance of the non-public class

javax.management.ClassAttributeValueExp

.

---

#### public static
QueryExp
not​(
QueryExp
queryExp)

Returns a constraint that is the negation of its argument.

**Parameters:**
- queryExp

- The constraint to negate.

**Returns:**
- A negated constraint. The returned object will be
serialized as an instance of the non-public class

javax.management.NotQueryExp

.

---

#### public static
QueryExp
in​(
ValueExp
val,

ValueExp
[] valueList)

Returns an expression constraining a value to be one of an explicit list.

**Parameters:**
- val

- A value to be constrained.
- valueList

- An array of ValueExps.

**Returns:**
- A QueryExp that represents the constraint. The
returned object will be serialized as an instance of the
non-public class

javax.management.InQueryExp

.

---

#### public static
StringValueExp
value​(
String
val)

Returns a new string expression.

**Parameters:**
- val

- The string value.

**Returns:**
- A ValueExp object containing the string argument.

---

#### public static
ValueExp
value​(
Number
val)

Returns a numeric value expression that can be used in any Query call
that expects a ValueExp.

**Parameters:**
- val

- An instance of Number.

**Returns:**
- A ValueExp object containing the argument. The
returned object will be serialized as an instance of the
non-public class

javax.management.NumericValueExp

.

---

#### public static
ValueExp
value​(int val)

Returns a numeric value expression that can be used in any Query call
that expects a ValueExp.

**Parameters:**
- val

- An int value.

**Returns:**
- A ValueExp object containing the argument. The
returned object will be serialized as an instance of the
non-public class

javax.management.NumericValueExp

.

---

#### public static
ValueExp
value​(long val)

Returns a numeric value expression that can be used in any Query call
that expects a ValueExp.

**Parameters:**
- val

- A long value.

**Returns:**
- A ValueExp object containing the argument. The
returned object will be serialized as an instance of the
non-public class

javax.management.NumericValueExp

.

---

#### public static
ValueExp
value​(float val)

Returns a numeric value expression that can be used in any Query call
that expects a ValueExp.

**Parameters:**
- val

- A float value.

**Returns:**
- A ValueExp object containing the argument. The
returned object will be serialized as an instance of the
non-public class

javax.management.NumericValueExp

.

---

#### public static
ValueExp
value​(double val)

Returns a numeric value expression that can be used in any Query call
that expects a ValueExp.

**Parameters:**
- val

- A double value.

**Returns:**
- A ValueExp object containing the argument. The
returned object will be serialized as an instance of the
non-public class

javax.management.NumericValueExp

.

---

#### public static
ValueExp
value​(boolean val)

Returns a boolean value expression that can be used in any Query call
that expects a ValueExp.

**Parameters:**
- val

- A boolean value.

**Returns:**
- A ValueExp object containing the argument. The
returned object will be serialized as an instance of the
non-public class

javax.management.BooleanValueExp

.

---

#### public static
ValueExp
plus​(
ValueExp
value1,

ValueExp
value2)

Returns a binary expression representing the sum of two numeric values,
or the concatenation of two string values.

**Parameters:**
- value1

- The first '+' operand.
- value2

- The second '+' operand.

**Returns:**
- A ValueExp representing the sum or concatenation of
the two arguments. The returned object will be serialized as
an instance of the non-public class

javax.management.BinaryOpValueExp

with an

op

equal to

PLUS

.

---

#### public static
ValueExp
times​(
ValueExp
value1,

ValueExp
value2)

Returns a binary expression representing the product of two numeric values.

**Parameters:**
- value1

- The first '*' operand.
- value2

- The second '*' operand.

**Returns:**
- A ValueExp representing the product. The returned
object will be serialized as an instance of the non-public
class

javax.management.BinaryOpValueExp

with an

op

equal to

TIMES

.

---

#### public static
ValueExp
minus​(
ValueExp
value1,

ValueExp
value2)

Returns a binary expression representing the difference between two numeric
values.

**Parameters:**
- value1

- The first '-' operand.
- value2

- The second '-' operand.

**Returns:**
- A ValueExp representing the difference between two
arguments. The returned object will be serialized as an
instance of the non-public class

javax.management.BinaryOpValueExp

with an

op

equal to

MINUS

.

---

#### public static
ValueExp
div​(
ValueExp
value1,

ValueExp
value2)

Returns a binary expression representing the quotient of two numeric
values.

**Parameters:**
- value1

- The first '/' operand.
- value2

- The second '/' operand.

**Returns:**
- A ValueExp representing the quotient of two arguments.
The returned object will be serialized as an instance of the
non-public class

javax.management.BinaryOpValueExp

with an

op

equal to

DIV

.

---

#### public static
QueryExp
initialSubString​(
AttributeValueExp
a,

StringValueExp
s)

Returns a query expression that represents a matching constraint on
a string argument. The value must start with the given literal string
value.

**Parameters:**
- a

- An attribute expression.
- s

- A string value expression representing the beginning of the
string value.

**Returns:**
- The constraint that a matches s. The returned object
will be serialized as an instance of the non-public class

javax.management.MatchQueryExp

.

---

#### public static
QueryExp
anySubString​(
AttributeValueExp
a,

StringValueExp
s)

Returns a query expression that represents a matching constraint on
a string argument. The value must contain the given literal string
value.

**Parameters:**
- a

- An attribute expression.
- s

- A string value expression representing the substring.

**Returns:**
- The constraint that a matches s. The returned object
will be serialized as an instance of the non-public class

javax.management.MatchQueryExp

.

---

#### public static
QueryExp
finalSubString​(
AttributeValueExp
a,

StringValueExp
s)

Returns a query expression that represents a matching constraint on
a string argument. The value must end with the given literal string
value.

**Parameters:**
- a

- An attribute expression.
- s

- A string value expression representing the end of the string
value.

**Returns:**
- The constraint that a matches s. The returned object
will be serialized as an instance of the non-public class

javax.management.MatchQueryExp

.

---

#### public static
QueryExp
isInstanceOf​(
StringValueExp
classNameValue)

Returns a query expression that represents an inheritance constraint
on an MBean class.

Example: to find MBeans that are instances of

NotificationBroadcaster

, use

Query.isInstanceOf(Query.value(NotificationBroadcaster.class.getName()))

.

Evaluating this expression for a given

objectName

includes performing

MBeanServer.isInstanceOf(objectName,
((StringValueExp)classNameValue.apply(objectName)).getValue()

.

**Parameters:**
- classNameValue

- The

StringValueExp

returning the name
of the class of which selected MBeans should be instances.

**Returns:**
- a query expression that represents an inheritance
constraint on an MBean class. The returned object will be
serialized as an instance of the non-public class

javax.management.InstanceOfQueryExp

.

**Since:**
- 1.6

---

### Additional Sections

#### Class Query

java.lang.Object

- javax.management.Query

javax.management.Query

```java
public class
Query

extends
Object
```

Constructs query object constraints.

The MBean Server can be queried for MBeans that meet a particular
condition, using its

queryNames

or

queryMBeans

method. The

QueryExp

parameter to the method can be any implementation of the interface

QueryExp

, but it is usually best to obtain the

QueryExp

value by calling the static methods in this class. This is particularly
true when querying a remote MBean Server: a custom implementation of the

QueryExp

interface might not be present in the remote MBean Server,
but the methods in this class return only standard classes that are
part of the JMX implementation.

As an example, suppose you wanted to find all MBeans where the

Enabled

attribute is

true

and the

Owner

attribute is

"Duke"

. Here is how you could construct the appropriate

QueryExp

by
chaining together method calls:

```java
QueryExp query =
Query.and(Query.eq(Query.attr("Enabled"), Query.value(true)),
Query.eq(Query.attr("Owner"), Query.value("Duke")));
```

**Since:** 1.5

public class

Query

extends

Object

Constructs query object constraints.

The MBean Server can be queried for MBeans that meet a particular
condition, using its

queryNames

or

queryMBeans

method. The

QueryExp

parameter to the method can be any implementation of the interface

QueryExp

, but it is usually best to obtain the

QueryExp

value by calling the static methods in this class. This is particularly
true when querying a remote MBean Server: a custom implementation of the

QueryExp

interface might not be present in the remote MBean Server,
but the methods in this class return only standard classes that are
part of the JMX implementation.

As an example, suppose you wanted to find all MBeans where the

Enabled

attribute is

true

and the

Owner

attribute is

"Duke"

. Here is how you could construct the appropriate

QueryExp

by
chaining together method calls:

```java
QueryExp query =
Query.and(Query.eq(Query.attr("Enabled"), Query.value(true)),
Query.eq(Query.attr("Owner"), Query.value("Duke")));
```

Constructs query object constraints.

The MBean Server can be queried for MBeans that meet a particular
condition, using its

queryNames

or

queryMBeans

method. The

QueryExp

parameter to the method can be any implementation of the interface

QueryExp

, but it is usually best to obtain the

QueryExp

value by calling the static methods in this class. This is particularly
true when querying a remote MBean Server: a custom implementation of the

QueryExp

interface might not be present in the remote MBean Server,
but the methods in this class return only standard classes that are
part of the JMX implementation.

As an example, suppose you wanted to find all MBeans where the

Enabled

attribute is

true

and the

Owner

attribute is

"Duke"

. Here is how you could construct the appropriate

QueryExp

by
chaining together method calls:

QueryExp query =
Query.and(Query.eq(Query.attr("Enabled"), Query.value(true)),
Query.eq(Query.attr("Owner"), Query.value("Duke")));

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

DIV

A code representing the

div(javax.management.ValueExp, javax.management.ValueExp)

expression.

static int

EQ

A code representing the

eq(javax.management.ValueExp, javax.management.ValueExp)

query.

static int

GE

A code representing the

geq(javax.management.ValueExp, javax.management.ValueExp)

query.

static int

GT

A code representing the

gt(javax.management.ValueExp, javax.management.ValueExp)

query.

static int

LE

A code representing the

leq(javax.management.ValueExp, javax.management.ValueExp)

query.

static int

LT

A code representing the

lt(javax.management.ValueExp, javax.management.ValueExp)

query.

static int

MINUS

A code representing the

minus(javax.management.ValueExp, javax.management.ValueExp)

expression.

static int

PLUS

A code representing the

plus(javax.management.ValueExp, javax.management.ValueExp)

expression.

static int

TIMES

A code representing the

times(javax.management.ValueExp, javax.management.ValueExp)

expression.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Query

()

Basic constructor.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

QueryExp

and

​(

QueryExp

q1,

QueryExp

q2)

Returns a query expression that is the conjunction of two other query
expressions.

static

QueryExp

anySubString

​(

AttributeValueExp

a,

StringValueExp

s)

Returns a query expression that represents a matching constraint on
a string argument.

static

AttributeValueExp

attr

​(

String

name)

Returns a new attribute expression.

static

AttributeValueExp

attr

​(

String

className,

String

name)

Returns a new qualified attribute expression.

static

QueryExp

between

​(

ValueExp

v1,

ValueExp

v2,

ValueExp

v3)

Returns a query expression that represents the constraint that one
value is between two other values.

static

AttributeValueExp

classattr

()

Returns a new class attribute expression which can be used in any
Query call that expects a ValueExp.

static

ValueExp

div

​(

ValueExp

value1,

ValueExp

value2)

Returns a binary expression representing the quotient of two numeric
values.

static

QueryExp

eq

​(

ValueExp

v1,

ValueExp

v2)

Returns a query expression that represents an equality constraint on
two values.

static

QueryExp

finalSubString

​(

AttributeValueExp

a,

StringValueExp

s)

Returns a query expression that represents a matching constraint on
a string argument.

static

QueryExp

geq

​(

ValueExp

v1,

ValueExp

v2)

Returns a query expression that represents a "greater than or equal
to" constraint on two values.

static

QueryExp

gt

​(

ValueExp

v1,

ValueExp

v2)

Returns a query expression that represents a "greater than" constraint on
two values.

static

QueryExp

in

​(

ValueExp

val,

ValueExp

[] valueList)

Returns an expression constraining a value to be one of an explicit list.

static

QueryExp

initialSubString

​(

AttributeValueExp

a,

StringValueExp

s)

Returns a query expression that represents a matching constraint on
a string argument.

static

QueryExp

isInstanceOf

​(

StringValueExp

classNameValue)

Returns a query expression that represents an inheritance constraint
on an MBean class.

static

QueryExp

leq

​(

ValueExp

v1,

ValueExp

v2)

Returns a query expression that represents a "less than or equal to"
constraint on two values.

static

QueryExp

lt

​(

ValueExp

v1,

ValueExp

v2)

Returns a query expression that represents a "less than" constraint on
two values.

static

QueryExp

match

​(

AttributeValueExp

a,

StringValueExp

s)

Returns a query expression that represents a matching constraint on
a string argument.

static

ValueExp

minus

​(

ValueExp

value1,

ValueExp

value2)

Returns a binary expression representing the difference between two numeric
values.

static

QueryExp

not

​(

QueryExp

queryExp)

Returns a constraint that is the negation of its argument.

static

QueryExp

or

​(

QueryExp

q1,

QueryExp

q2)

Returns a query expression that is the disjunction of two other query
expressions.

static

ValueExp

plus

​(

ValueExp

value1,

ValueExp

value2)

Returns a binary expression representing the sum of two numeric values,
or the concatenation of two string values.

static

ValueExp

times

​(

ValueExp

value1,

ValueExp

value2)

Returns a binary expression representing the product of two numeric values.

static

ValueExp

value

​(boolean val)

Returns a boolean value expression that can be used in any Query call
that expects a ValueExp.

static

ValueExp

value

​(double val)

Returns a numeric value expression that can be used in any Query call
that expects a ValueExp.

static

ValueExp

value

​(float val)

Returns a numeric value expression that can be used in any Query call
that expects a ValueExp.

static

ValueExp

value

​(int val)

Returns a numeric value expression that can be used in any Query call
that expects a ValueExp.

static

ValueExp

value

​(long val)

Returns a numeric value expression that can be used in any Query call
that expects a ValueExp.

static

ValueExp

value

​(

Number

val)

Returns a numeric value expression that can be used in any Query call
that expects a ValueExp.

static

StringValueExp

value

​(

String

val)

Returns a new string expression.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Field Summary

Fields

Modifier and Type

Field

Description

static int

DIV

A code representing the

div(javax.management.ValueExp, javax.management.ValueExp)

expression.

static int

EQ

A code representing the

eq(javax.management.ValueExp, javax.management.ValueExp)

query.

static int

GE

A code representing the

geq(javax.management.ValueExp, javax.management.ValueExp)

query.

static int

GT

A code representing the

gt(javax.management.ValueExp, javax.management.ValueExp)

query.

static int

LE

A code representing the

leq(javax.management.ValueExp, javax.management.ValueExp)

query.

static int

LT

A code representing the

lt(javax.management.ValueExp, javax.management.ValueExp)

query.

static int

MINUS

A code representing the

minus(javax.management.ValueExp, javax.management.ValueExp)

expression.

static int

PLUS

A code representing the

plus(javax.management.ValueExp, javax.management.ValueExp)

expression.

static int

TIMES

A code representing the

times(javax.management.ValueExp, javax.management.ValueExp)

expression.

---

#### Field Summary

A code representing the

div(javax.management.ValueExp, javax.management.ValueExp)

expression.

A code representing the

eq(javax.management.ValueExp, javax.management.ValueExp)

query.

A code representing the

geq(javax.management.ValueExp, javax.management.ValueExp)

query.

A code representing the

gt(javax.management.ValueExp, javax.management.ValueExp)

query.

A code representing the

leq(javax.management.ValueExp, javax.management.ValueExp)

query.

A code representing the

lt(javax.management.ValueExp, javax.management.ValueExp)

query.

A code representing the

minus(javax.management.ValueExp, javax.management.ValueExp)

expression.

A code representing the

plus(javax.management.ValueExp, javax.management.ValueExp)

expression.

A code representing the

times(javax.management.ValueExp, javax.management.ValueExp)

expression.

Constructor Summary

Constructors

Constructor

Description

Query

()

Basic constructor.

---

#### Constructor Summary

Basic constructor.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

QueryExp

and

​(

QueryExp

q1,

QueryExp

q2)

Returns a query expression that is the conjunction of two other query
expressions.

static

QueryExp

anySubString

​(

AttributeValueExp

a,

StringValueExp

s)

Returns a query expression that represents a matching constraint on
a string argument.

static

AttributeValueExp

attr

​(

String

name)

Returns a new attribute expression.

static

AttributeValueExp

attr

​(

String

className,

String

name)

Returns a new qualified attribute expression.

static

QueryExp

between

​(

ValueExp

v1,

ValueExp

v2,

ValueExp

v3)

Returns a query expression that represents the constraint that one
value is between two other values.

static

AttributeValueExp

classattr

()

Returns a new class attribute expression which can be used in any
Query call that expects a ValueExp.

static

ValueExp

div

​(

ValueExp

value1,

ValueExp

value2)

Returns a binary expression representing the quotient of two numeric
values.

static

QueryExp

eq

​(

ValueExp

v1,

ValueExp

v2)

Returns a query expression that represents an equality constraint on
two values.

static

QueryExp

finalSubString

​(

AttributeValueExp

a,

StringValueExp

s)

Returns a query expression that represents a matching constraint on
a string argument.

static

QueryExp

geq

​(

ValueExp

v1,

ValueExp

v2)

Returns a query expression that represents a "greater than or equal
to" constraint on two values.

static

QueryExp

gt

​(

ValueExp

v1,

ValueExp

v2)

Returns a query expression that represents a "greater than" constraint on
two values.

static

QueryExp

in

​(

ValueExp

val,

ValueExp

[] valueList)

Returns an expression constraining a value to be one of an explicit list.

static

QueryExp

initialSubString

​(

AttributeValueExp

a,

StringValueExp

s)

Returns a query expression that represents a matching constraint on
a string argument.

static

QueryExp

isInstanceOf

​(

StringValueExp

classNameValue)

Returns a query expression that represents an inheritance constraint
on an MBean class.

static

QueryExp

leq

​(

ValueExp

v1,

ValueExp

v2)

Returns a query expression that represents a "less than or equal to"
constraint on two values.

static

QueryExp

lt

​(

ValueExp

v1,

ValueExp

v2)

Returns a query expression that represents a "less than" constraint on
two values.

static

QueryExp

match

​(

AttributeValueExp

a,

StringValueExp

s)

Returns a query expression that represents a matching constraint on
a string argument.

static

ValueExp

minus

​(

ValueExp

value1,

ValueExp

value2)

Returns a binary expression representing the difference between two numeric
values.

static

QueryExp

not

​(

QueryExp

queryExp)

Returns a constraint that is the negation of its argument.

static

QueryExp

or

​(

QueryExp

q1,

QueryExp

q2)

Returns a query expression that is the disjunction of two other query
expressions.

static

ValueExp

plus

​(

ValueExp

value1,

ValueExp

value2)

Returns a binary expression representing the sum of two numeric values,
or the concatenation of two string values.

static

ValueExp

times

​(

ValueExp

value1,

ValueExp

value2)

Returns a binary expression representing the product of two numeric values.

static

ValueExp

value

​(boolean val)

Returns a boolean value expression that can be used in any Query call
that expects a ValueExp.

static

ValueExp

value

​(double val)

Returns a numeric value expression that can be used in any Query call
that expects a ValueExp.

static

ValueExp

value

​(float val)

Returns a numeric value expression that can be used in any Query call
that expects a ValueExp.

static

ValueExp

value

​(int val)

Returns a numeric value expression that can be used in any Query call
that expects a ValueExp.

static

ValueExp

value

​(long val)

Returns a numeric value expression that can be used in any Query call
that expects a ValueExp.

static

ValueExp

value

​(

Number

val)

Returns a numeric value expression that can be used in any Query call
that expects a ValueExp.

static

StringValueExp

value

​(

String

val)

Returns a new string expression.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Returns a query expression that is the conjunction of two other query
expressions.

Returns a query expression that represents a matching constraint on
a string argument.

Returns a new attribute expression.

Returns a new qualified attribute expression.

Returns a query expression that represents the constraint that one
value is between two other values.

Returns a new class attribute expression which can be used in any
Query call that expects a ValueExp.

Returns a binary expression representing the quotient of two numeric
values.

Returns a query expression that represents an equality constraint on
two values.

Returns a query expression that represents a "greater than or equal
to" constraint on two values.

Returns a query expression that represents a "greater than" constraint on
two values.

Returns an expression constraining a value to be one of an explicit list.

Returns a query expression that represents an inheritance constraint
on an MBean class.

Returns a query expression that represents a "less than or equal to"
constraint on two values.

Returns a query expression that represents a "less than" constraint on
two values.

Returns a binary expression representing the difference between two numeric
values.

Returns a constraint that is the negation of its argument.

Returns a query expression that is the disjunction of two other query
expressions.

Returns a binary expression representing the sum of two numeric values,
or the concatenation of two string values.

Returns a binary expression representing the product of two numeric values.

Returns a boolean value expression that can be used in any Query call
that expects a ValueExp.

Returns a numeric value expression that can be used in any Query call
that expects a ValueExp.

Returns a new string expression.

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ FIELD DETAIL ===========

- Field Detail

- GT

```java
public static final int GT
```

A code representing the

gt(javax.management.ValueExp, javax.management.ValueExp)

query. This is chiefly
of interest for the serialized form of queries.

**See Also:** Constant Field Values

- LT

```java
public static final int LT
```

A code representing the

lt(javax.management.ValueExp, javax.management.ValueExp)

query. This is chiefly
of interest for the serialized form of queries.

**See Also:** Constant Field Values

- GE

```java
public static final int GE
```

A code representing the

geq(javax.management.ValueExp, javax.management.ValueExp)

query. This is chiefly
of interest for the serialized form of queries.

**See Also:** Constant Field Values

- LE

```java
public static final int LE
```

A code representing the

leq(javax.management.ValueExp, javax.management.ValueExp)

query. This is chiefly
of interest for the serialized form of queries.

**See Also:** Constant Field Values

- EQ

```java
public static final int EQ
```

A code representing the

eq(javax.management.ValueExp, javax.management.ValueExp)

query. This is chiefly
of interest for the serialized form of queries.

**See Also:** Constant Field Values

- PLUS

```java
public static final int PLUS
```

A code representing the

plus(javax.management.ValueExp, javax.management.ValueExp)

expression. This
is chiefly of interest for the serialized form of queries.

**See Also:** Constant Field Values

- MINUS

```java
public static final int MINUS
```

A code representing the

minus(javax.management.ValueExp, javax.management.ValueExp)

expression. This
is chiefly of interest for the serialized form of queries.

**See Also:** Constant Field Values

- TIMES

```java
public static final int TIMES
```

A code representing the

times(javax.management.ValueExp, javax.management.ValueExp)

expression. This
is chiefly of interest for the serialized form of queries.

**See Also:** Constant Field Values

- DIV

```java
public static final int DIV
```

A code representing the

div(javax.management.ValueExp, javax.management.ValueExp)

expression. This is
chiefly of interest for the serialized form of queries.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Query

```java
public Query()
```

Basic constructor.

============ METHOD DETAIL ==========

- Method Detail

- and

```java
public static
QueryExp
and​(
QueryExp
q1,

QueryExp
q2)
```

Returns a query expression that is the conjunction of two other query
expressions.

**Parameters:** q1

- A query expression.
**Parameters:** q2

- Another query expression.
**Returns:** The conjunction of the two arguments. The returned object
will be serialized as an instance of the non-public class

javax.management.AndQueryExp

.

- or

```java
public static
QueryExp
or​(
QueryExp
q1,

QueryExp
q2)
```

Returns a query expression that is the disjunction of two other query
expressions.

**Parameters:** q1

- A query expression.
**Parameters:** q2

- Another query expression.
**Returns:** The disjunction of the two arguments. The returned object
will be serialized as an instance of the non-public class

javax.management.OrQueryExp

.

- gt

```java
public static
QueryExp
gt​(
ValueExp
v1,

ValueExp
v2)
```

Returns a query expression that represents a "greater than" constraint on
two values.

**Parameters:** v1

- A value expression.
**Parameters:** v2

- Another value expression.
**Returns:** A "greater than" constraint on the arguments. The
returned object will be serialized as an instance of the
non-public class

javax.management.BinaryRelQueryExp

with a

relOp

equal
to

GT

.

- geq

```java
public static
QueryExp
geq​(
ValueExp
v1,

ValueExp
v2)
```

Returns a query expression that represents a "greater than or equal
to" constraint on two values.

**Parameters:** v1

- A value expression.
**Parameters:** v2

- Another value expression.
**Returns:** A "greater than or equal to" constraint on the
arguments. The returned object will be serialized as an
instance of the non-public class

javax.management.BinaryRelQueryExp

with a

relOp

equal
to

GE

.

- leq

```java
public static
QueryExp
leq​(
ValueExp
v1,

ValueExp
v2)
```

Returns a query expression that represents a "less than or equal to"
constraint on two values.

**Parameters:** v1

- A value expression.
**Parameters:** v2

- Another value expression.
**Returns:** A "less than or equal to" constraint on the arguments.
The returned object will be serialized as an instance of the
non-public class

javax.management.BinaryRelQueryExp

with a

relOp

equal
to

LE

.

- lt

```java
public static
QueryExp
lt​(
ValueExp
v1,

ValueExp
v2)
```

Returns a query expression that represents a "less than" constraint on
two values.

**Parameters:** v1

- A value expression.
**Parameters:** v2

- Another value expression.
**Returns:** A "less than" constraint on the arguments. The
returned object will be serialized as an instance of the
non-public class

javax.management.BinaryRelQueryExp

with a

relOp

equal
to

LT

.

- eq

```java
public static
QueryExp
eq​(
ValueExp
v1,

ValueExp
v2)
```

Returns a query expression that represents an equality constraint on
two values.

**Parameters:** v1

- A value expression.
**Parameters:** v2

- Another value expression.
**Returns:** A "equal to" constraint on the arguments. The
returned object will be serialized as an instance of the
non-public class

javax.management.BinaryRelQueryExp

with a

relOp

equal
to

EQ

.

- between

```java
public static
QueryExp
between​(
ValueExp
v1,

ValueExp
v2,

ValueExp
v3)
```

Returns a query expression that represents the constraint that one
value is between two other values.

**Parameters:** v1

- A value expression that is "between" v2 and v3.
**Parameters:** v2

- Value expression that represents a boundary of the constraint.
**Parameters:** v3

- Value expression that represents a boundary of the constraint.
**Returns:** The constraint that v1 lies between v2 and v3. The
returned object will be serialized as an instance of the
non-public class

javax.management.BetweenQueryExp

.

- match

```java
public static
QueryExp
match​(
AttributeValueExp
a,

StringValueExp
s)
```

Returns a query expression that represents a matching constraint on
a string argument. The matching syntax is consistent with file globbing:
supports "

?

", "

*

", "

[

",
each of which may be escaped with "

\

";
character classes may use "

!

" for negation and
"

-

" for range.
(

*

for any character sequence,

?

for a single arbitrary character,

[...]

for a character sequence).
For example:

a*b?c

would match a string starting
with the character

a

, followed
by any number of characters, followed by a

b

,
any single character, and a

c

.

**Parameters:** a

- An attribute expression
**Parameters:** s

- A string value expression representing a matching constraint
**Returns:** A query expression that represents the matching
constraint on the string argument. The returned object will
be serialized as an instance of the non-public class

javax.management.MatchQueryExp

.

- attr

```java
public static
AttributeValueExp
attr​(
String
name)
```

Returns a new attribute expression. See

AttributeValueExp

for a detailed description of the semantics of the expression.

Evaluating this expression for a given

objectName

includes performing

MBeanServer.getAttribute(objectName,
name)

.

**Parameters:** name

- The name of the attribute.
**Returns:** An attribute expression for the attribute named

name

.

- attr

```java
public static
AttributeValueExp
attr​(
String
className,

String
name)
```

Returns a new qualified attribute expression.

Evaluating this expression for a given

objectName

includes performing

MBeanServer.getObjectInstance(objectName)

and

MBeanServer.getAttribute(objectName,
name)

.

**Parameters:** className

- The name of the class possessing the attribute.
**Parameters:** name

- The name of the attribute.
**Returns:** An attribute expression for the attribute named name.
The returned object will be serialized as an instance of the
non-public class

javax.management.QualifiedAttributeValueExp

.

- classattr

```java
public static
AttributeValueExp
classattr()
```

Returns a new class attribute expression which can be used in any
Query call that expects a ValueExp.

Evaluating this expression for a given

objectName

includes performing

MBeanServer.getObjectInstance(objectName)

.

**Returns:** A class attribute expression. The returned object
will be serialized as an instance of the non-public class

javax.management.ClassAttributeValueExp

.

- not

```java
public static
QueryExp
not​(
QueryExp
queryExp)
```

Returns a constraint that is the negation of its argument.

**Parameters:** queryExp

- The constraint to negate.
**Returns:** A negated constraint. The returned object will be
serialized as an instance of the non-public class

javax.management.NotQueryExp

.

- in

```java
public static
QueryExp
in​(
ValueExp
val,

ValueExp
[] valueList)
```

Returns an expression constraining a value to be one of an explicit list.

**Parameters:** val

- A value to be constrained.
**Parameters:** valueList

- An array of ValueExps.
**Returns:** A QueryExp that represents the constraint. The
returned object will be serialized as an instance of the
non-public class

javax.management.InQueryExp

.

- value

```java
public static
StringValueExp
value​(
String
val)
```

Returns a new string expression.

**Parameters:** val

- The string value.
**Returns:** A ValueExp object containing the string argument.

- value

```java
public static
ValueExp
value​(
Number
val)
```

Returns a numeric value expression that can be used in any Query call
that expects a ValueExp.

**Parameters:** val

- An instance of Number.
**Returns:** A ValueExp object containing the argument. The
returned object will be serialized as an instance of the
non-public class

javax.management.NumericValueExp

.

- value

```java
public static
ValueExp
value​(int val)
```

Returns a numeric value expression that can be used in any Query call
that expects a ValueExp.

**Parameters:** val

- An int value.
**Returns:** A ValueExp object containing the argument. The
returned object will be serialized as an instance of the
non-public class

javax.management.NumericValueExp

.

- value

```java
public static
ValueExp
value​(long val)
```

Returns a numeric value expression that can be used in any Query call
that expects a ValueExp.

**Parameters:** val

- A long value.
**Returns:** A ValueExp object containing the argument. The
returned object will be serialized as an instance of the
non-public class

javax.management.NumericValueExp

.

- value

```java
public static
ValueExp
value​(float val)
```

Returns a numeric value expression that can be used in any Query call
that expects a ValueExp.

**Parameters:** val

- A float value.
**Returns:** A ValueExp object containing the argument. The
returned object will be serialized as an instance of the
non-public class

javax.management.NumericValueExp

.

- value

```java
public static
ValueExp
value​(double val)
```

Returns a numeric value expression that can be used in any Query call
that expects a ValueExp.

**Parameters:** val

- A double value.
**Returns:** A ValueExp object containing the argument. The
returned object will be serialized as an instance of the
non-public class

javax.management.NumericValueExp

.

- value

```java
public static
ValueExp
value​(boolean val)
```

Returns a boolean value expression that can be used in any Query call
that expects a ValueExp.

**Parameters:** val

- A boolean value.
**Returns:** A ValueExp object containing the argument. The
returned object will be serialized as an instance of the
non-public class

javax.management.BooleanValueExp

.

- plus

```java
public static
ValueExp
plus​(
ValueExp
value1,

ValueExp
value2)
```

Returns a binary expression representing the sum of two numeric values,
or the concatenation of two string values.

**Parameters:** value1

- The first '+' operand.
**Parameters:** value2

- The second '+' operand.
**Returns:** A ValueExp representing the sum or concatenation of
the two arguments. The returned object will be serialized as
an instance of the non-public class

javax.management.BinaryOpValueExp

with an

op

equal to

PLUS

.

- times

```java
public static
ValueExp
times​(
ValueExp
value1,

ValueExp
value2)
```

Returns a binary expression representing the product of two numeric values.

**Parameters:** value1

- The first '*' operand.
**Parameters:** value2

- The second '*' operand.
**Returns:** A ValueExp representing the product. The returned
object will be serialized as an instance of the non-public
class

javax.management.BinaryOpValueExp

with an

op

equal to

TIMES

.

- minus

```java
public static
ValueExp
minus​(
ValueExp
value1,

ValueExp
value2)
```

Returns a binary expression representing the difference between two numeric
values.

**Parameters:** value1

- The first '-' operand.
**Parameters:** value2

- The second '-' operand.
**Returns:** A ValueExp representing the difference between two
arguments. The returned object will be serialized as an
instance of the non-public class

javax.management.BinaryOpValueExp

with an

op

equal to

MINUS

.

- div

```java
public static
ValueExp
div​(
ValueExp
value1,

ValueExp
value2)
```

Returns a binary expression representing the quotient of two numeric
values.

**Parameters:** value1

- The first '/' operand.
**Parameters:** value2

- The second '/' operand.
**Returns:** A ValueExp representing the quotient of two arguments.
The returned object will be serialized as an instance of the
non-public class

javax.management.BinaryOpValueExp

with an

op

equal to

DIV

.

- initialSubString

```java
public static
QueryExp
initialSubString​(
AttributeValueExp
a,

StringValueExp
s)
```

Returns a query expression that represents a matching constraint on
a string argument. The value must start with the given literal string
value.

**Parameters:** a

- An attribute expression.
**Parameters:** s

- A string value expression representing the beginning of the
string value.
**Returns:** The constraint that a matches s. The returned object
will be serialized as an instance of the non-public class

javax.management.MatchQueryExp

.

- anySubString

```java
public static
QueryExp
anySubString​(
AttributeValueExp
a,

StringValueExp
s)
```

Returns a query expression that represents a matching constraint on
a string argument. The value must contain the given literal string
value.

**Parameters:** a

- An attribute expression.
**Parameters:** s

- A string value expression representing the substring.
**Returns:** The constraint that a matches s. The returned object
will be serialized as an instance of the non-public class

javax.management.MatchQueryExp

.

- finalSubString

```java
public static
QueryExp
finalSubString​(
AttributeValueExp
a,

StringValueExp
s)
```

Returns a query expression that represents a matching constraint on
a string argument. The value must end with the given literal string
value.

**Parameters:** a

- An attribute expression.
**Parameters:** s

- A string value expression representing the end of the string
value.
**Returns:** The constraint that a matches s. The returned object
will be serialized as an instance of the non-public class

javax.management.MatchQueryExp

.

- isInstanceOf

```java
public static
QueryExp
isInstanceOf​(
StringValueExp
classNameValue)
```

Returns a query expression that represents an inheritance constraint
on an MBean class.

Example: to find MBeans that are instances of

NotificationBroadcaster

, use

Query.isInstanceOf(Query.value(NotificationBroadcaster.class.getName()))

.

Evaluating this expression for a given

objectName

includes performing

MBeanServer.isInstanceOf(objectName,
((StringValueExp)classNameValue.apply(objectName)).getValue()

.

**Parameters:** classNameValue

- The

StringValueExp

returning the name
of the class of which selected MBeans should be instances.
**Returns:** a query expression that represents an inheritance
constraint on an MBean class. The returned object will be
serialized as an instance of the non-public class

javax.management.InstanceOfQueryExp

.
**Since:** 1.6

Field Detail

- GT

```java
public static final int GT
```

A code representing the

gt(javax.management.ValueExp, javax.management.ValueExp)

query. This is chiefly
of interest for the serialized form of queries.

**See Also:** Constant Field Values

- LT

```java
public static final int LT
```

A code representing the

lt(javax.management.ValueExp, javax.management.ValueExp)

query. This is chiefly
of interest for the serialized form of queries.

**See Also:** Constant Field Values

- GE

```java
public static final int GE
```

A code representing the

geq(javax.management.ValueExp, javax.management.ValueExp)

query. This is chiefly
of interest for the serialized form of queries.

**See Also:** Constant Field Values

- LE

```java
public static final int LE
```

A code representing the

leq(javax.management.ValueExp, javax.management.ValueExp)

query. This is chiefly
of interest for the serialized form of queries.

**See Also:** Constant Field Values

- EQ

```java
public static final int EQ
```

A code representing the

eq(javax.management.ValueExp, javax.management.ValueExp)

query. This is chiefly
of interest for the serialized form of queries.

**See Also:** Constant Field Values

- PLUS

```java
public static final int PLUS
```

A code representing the

plus(javax.management.ValueExp, javax.management.ValueExp)

expression. This
is chiefly of interest for the serialized form of queries.

**See Also:** Constant Field Values

- MINUS

```java
public static final int MINUS
```

A code representing the

minus(javax.management.ValueExp, javax.management.ValueExp)

expression. This
is chiefly of interest for the serialized form of queries.

**See Also:** Constant Field Values

- TIMES

```java
public static final int TIMES
```

A code representing the

times(javax.management.ValueExp, javax.management.ValueExp)

expression. This
is chiefly of interest for the serialized form of queries.

**See Also:** Constant Field Values

- DIV

```java
public static final int DIV
```

A code representing the

div(javax.management.ValueExp, javax.management.ValueExp)

expression. This is
chiefly of interest for the serialized form of queries.

**See Also:** Constant Field Values

---

#### Field Detail

GT

```java
public static final int GT
```

A code representing the

gt(javax.management.ValueExp, javax.management.ValueExp)

query. This is chiefly
of interest for the serialized form of queries.

**See Also:** Constant Field Values

---

#### GT

public static final int GT

A code representing the

gt(javax.management.ValueExp, javax.management.ValueExp)

query. This is chiefly
of interest for the serialized form of queries.

LT

```java
public static final int LT
```

A code representing the

lt(javax.management.ValueExp, javax.management.ValueExp)

query. This is chiefly
of interest for the serialized form of queries.

**See Also:** Constant Field Values

---

#### LT

public static final int LT

A code representing the

lt(javax.management.ValueExp, javax.management.ValueExp)

query. This is chiefly
of interest for the serialized form of queries.

GE

```java
public static final int GE
```

A code representing the

geq(javax.management.ValueExp, javax.management.ValueExp)

query. This is chiefly
of interest for the serialized form of queries.

**See Also:** Constant Field Values

---

#### GE

public static final int GE

A code representing the

geq(javax.management.ValueExp, javax.management.ValueExp)

query. This is chiefly
of interest for the serialized form of queries.

LE

```java
public static final int LE
```

A code representing the

leq(javax.management.ValueExp, javax.management.ValueExp)

query. This is chiefly
of interest for the serialized form of queries.

**See Also:** Constant Field Values

---

#### LE

public static final int LE

A code representing the

leq(javax.management.ValueExp, javax.management.ValueExp)

query. This is chiefly
of interest for the serialized form of queries.

EQ

```java
public static final int EQ
```

A code representing the

eq(javax.management.ValueExp, javax.management.ValueExp)

query. This is chiefly
of interest for the serialized form of queries.

**See Also:** Constant Field Values

---

#### EQ

public static final int EQ

A code representing the

eq(javax.management.ValueExp, javax.management.ValueExp)

query. This is chiefly
of interest for the serialized form of queries.

PLUS

```java
public static final int PLUS
```

A code representing the

plus(javax.management.ValueExp, javax.management.ValueExp)

expression. This
is chiefly of interest for the serialized form of queries.

**See Also:** Constant Field Values

---

#### PLUS

public static final int PLUS

A code representing the

plus(javax.management.ValueExp, javax.management.ValueExp)

expression. This
is chiefly of interest for the serialized form of queries.

MINUS

```java
public static final int MINUS
```

A code representing the

minus(javax.management.ValueExp, javax.management.ValueExp)

expression. This
is chiefly of interest for the serialized form of queries.

**See Also:** Constant Field Values

---

#### MINUS

public static final int MINUS

A code representing the

minus(javax.management.ValueExp, javax.management.ValueExp)

expression. This
is chiefly of interest for the serialized form of queries.

TIMES

```java
public static final int TIMES
```

A code representing the

times(javax.management.ValueExp, javax.management.ValueExp)

expression. This
is chiefly of interest for the serialized form of queries.

**See Also:** Constant Field Values

---

#### TIMES

public static final int TIMES

A code representing the

times(javax.management.ValueExp, javax.management.ValueExp)

expression. This
is chiefly of interest for the serialized form of queries.

DIV

```java
public static final int DIV
```

A code representing the

div(javax.management.ValueExp, javax.management.ValueExp)

expression. This is
chiefly of interest for the serialized form of queries.

**See Also:** Constant Field Values

---

#### DIV

public static final int DIV

A code representing the

div(javax.management.ValueExp, javax.management.ValueExp)

expression. This is
chiefly of interest for the serialized form of queries.

Constructor Detail

- Query

```java
public Query()
```

Basic constructor.

---

#### Constructor Detail

Query

```java
public Query()
```

Basic constructor.

---

#### Query

public Query()

Basic constructor.

Method Detail

- and

```java
public static
QueryExp
and​(
QueryExp
q1,

QueryExp
q2)
```

Returns a query expression that is the conjunction of two other query
expressions.

**Parameters:** q1

- A query expression.
**Parameters:** q2

- Another query expression.
**Returns:** The conjunction of the two arguments. The returned object
will be serialized as an instance of the non-public class

javax.management.AndQueryExp

.

- or

```java
public static
QueryExp
or​(
QueryExp
q1,

QueryExp
q2)
```

Returns a query expression that is the disjunction of two other query
expressions.

**Parameters:** q1

- A query expression.
**Parameters:** q2

- Another query expression.
**Returns:** The disjunction of the two arguments. The returned object
will be serialized as an instance of the non-public class

javax.management.OrQueryExp

.

- gt

```java
public static
QueryExp
gt​(
ValueExp
v1,

ValueExp
v2)
```

Returns a query expression that represents a "greater than" constraint on
two values.

**Parameters:** v1

- A value expression.
**Parameters:** v2

- Another value expression.
**Returns:** A "greater than" constraint on the arguments. The
returned object will be serialized as an instance of the
non-public class

javax.management.BinaryRelQueryExp

with a

relOp

equal
to

GT

.

- geq

```java
public static
QueryExp
geq​(
ValueExp
v1,

ValueExp
v2)
```

Returns a query expression that represents a "greater than or equal
to" constraint on two values.

**Parameters:** v1

- A value expression.
**Parameters:** v2

- Another value expression.
**Returns:** A "greater than or equal to" constraint on the
arguments. The returned object will be serialized as an
instance of the non-public class

javax.management.BinaryRelQueryExp

with a

relOp

equal
to

GE

.

- leq

```java
public static
QueryExp
leq​(
ValueExp
v1,

ValueExp
v2)
```

Returns a query expression that represents a "less than or equal to"
constraint on two values.

**Parameters:** v1

- A value expression.
**Parameters:** v2

- Another value expression.
**Returns:** A "less than or equal to" constraint on the arguments.
The returned object will be serialized as an instance of the
non-public class

javax.management.BinaryRelQueryExp

with a

relOp

equal
to

LE

.

- lt

```java
public static
QueryExp
lt​(
ValueExp
v1,

ValueExp
v2)
```

Returns a query expression that represents a "less than" constraint on
two values.

**Parameters:** v1

- A value expression.
**Parameters:** v2

- Another value expression.
**Returns:** A "less than" constraint on the arguments. The
returned object will be serialized as an instance of the
non-public class

javax.management.BinaryRelQueryExp

with a

relOp

equal
to

LT

.

- eq

```java
public static
QueryExp
eq​(
ValueExp
v1,

ValueExp
v2)
```

Returns a query expression that represents an equality constraint on
two values.

**Parameters:** v1

- A value expression.
**Parameters:** v2

- Another value expression.
**Returns:** A "equal to" constraint on the arguments. The
returned object will be serialized as an instance of the
non-public class

javax.management.BinaryRelQueryExp

with a

relOp

equal
to

EQ

.

- between

```java
public static
QueryExp
between​(
ValueExp
v1,

ValueExp
v2,

ValueExp
v3)
```

Returns a query expression that represents the constraint that one
value is between two other values.

**Parameters:** v1

- A value expression that is "between" v2 and v3.
**Parameters:** v2

- Value expression that represents a boundary of the constraint.
**Parameters:** v3

- Value expression that represents a boundary of the constraint.
**Returns:** The constraint that v1 lies between v2 and v3. The
returned object will be serialized as an instance of the
non-public class

javax.management.BetweenQueryExp

.

- match

```java
public static
QueryExp
match​(
AttributeValueExp
a,

StringValueExp
s)
```

Returns a query expression that represents a matching constraint on
a string argument. The matching syntax is consistent with file globbing:
supports "

?

", "

*

", "

[

",
each of which may be escaped with "

\

";
character classes may use "

!

" for negation and
"

-

" for range.
(

*

for any character sequence,

?

for a single arbitrary character,

[...]

for a character sequence).
For example:

a*b?c

would match a string starting
with the character

a

, followed
by any number of characters, followed by a

b

,
any single character, and a

c

.

**Parameters:** a

- An attribute expression
**Parameters:** s

- A string value expression representing a matching constraint
**Returns:** A query expression that represents the matching
constraint on the string argument. The returned object will
be serialized as an instance of the non-public class

javax.management.MatchQueryExp

.

- attr

```java
public static
AttributeValueExp
attr​(
String
name)
```

Returns a new attribute expression. See

AttributeValueExp

for a detailed description of the semantics of the expression.

Evaluating this expression for a given

objectName

includes performing

MBeanServer.getAttribute(objectName,
name)

.

**Parameters:** name

- The name of the attribute.
**Returns:** An attribute expression for the attribute named

name

.

- attr

```java
public static
AttributeValueExp
attr​(
String
className,

String
name)
```

Returns a new qualified attribute expression.

Evaluating this expression for a given

objectName

includes performing

MBeanServer.getObjectInstance(objectName)

and

MBeanServer.getAttribute(objectName,
name)

.

**Parameters:** className

- The name of the class possessing the attribute.
**Parameters:** name

- The name of the attribute.
**Returns:** An attribute expression for the attribute named name.
The returned object will be serialized as an instance of the
non-public class

javax.management.QualifiedAttributeValueExp

.

- classattr

```java
public static
AttributeValueExp
classattr()
```

Returns a new class attribute expression which can be used in any
Query call that expects a ValueExp.

Evaluating this expression for a given

objectName

includes performing

MBeanServer.getObjectInstance(objectName)

.

**Returns:** A class attribute expression. The returned object
will be serialized as an instance of the non-public class

javax.management.ClassAttributeValueExp

.

- not

```java
public static
QueryExp
not​(
QueryExp
queryExp)
```

Returns a constraint that is the negation of its argument.

**Parameters:** queryExp

- The constraint to negate.
**Returns:** A negated constraint. The returned object will be
serialized as an instance of the non-public class

javax.management.NotQueryExp

.

- in

```java
public static
QueryExp
in​(
ValueExp
val,

ValueExp
[] valueList)
```

Returns an expression constraining a value to be one of an explicit list.

**Parameters:** val

- A value to be constrained.
**Parameters:** valueList

- An array of ValueExps.
**Returns:** A QueryExp that represents the constraint. The
returned object will be serialized as an instance of the
non-public class

javax.management.InQueryExp

.

- value

```java
public static
StringValueExp
value​(
String
val)
```

Returns a new string expression.

**Parameters:** val

- The string value.
**Returns:** A ValueExp object containing the string argument.

- value

```java
public static
ValueExp
value​(
Number
val)
```

Returns a numeric value expression that can be used in any Query call
that expects a ValueExp.

**Parameters:** val

- An instance of Number.
**Returns:** A ValueExp object containing the argument. The
returned object will be serialized as an instance of the
non-public class

javax.management.NumericValueExp

.

- value

```java
public static
ValueExp
value​(int val)
```

Returns a numeric value expression that can be used in any Query call
that expects a ValueExp.

**Parameters:** val

- An int value.
**Returns:** A ValueExp object containing the argument. The
returned object will be serialized as an instance of the
non-public class

javax.management.NumericValueExp

.

- value

```java
public static
ValueExp
value​(long val)
```

Returns a numeric value expression that can be used in any Query call
that expects a ValueExp.

**Parameters:** val

- A long value.
**Returns:** A ValueExp object containing the argument. The
returned object will be serialized as an instance of the
non-public class

javax.management.NumericValueExp

.

- value

```java
public static
ValueExp
value​(float val)
```

Returns a numeric value expression that can be used in any Query call
that expects a ValueExp.

**Parameters:** val

- A float value.
**Returns:** A ValueExp object containing the argument. The
returned object will be serialized as an instance of the
non-public class

javax.management.NumericValueExp

.

- value

```java
public static
ValueExp
value​(double val)
```

Returns a numeric value expression that can be used in any Query call
that expects a ValueExp.

**Parameters:** val

- A double value.
**Returns:** A ValueExp object containing the argument. The
returned object will be serialized as an instance of the
non-public class

javax.management.NumericValueExp

.

- value

```java
public static
ValueExp
value​(boolean val)
```

Returns a boolean value expression that can be used in any Query call
that expects a ValueExp.

**Parameters:** val

- A boolean value.
**Returns:** A ValueExp object containing the argument. The
returned object will be serialized as an instance of the
non-public class

javax.management.BooleanValueExp

.

- plus

```java
public static
ValueExp
plus​(
ValueExp
value1,

ValueExp
value2)
```

Returns a binary expression representing the sum of two numeric values,
or the concatenation of two string values.

**Parameters:** value1

- The first '+' operand.
**Parameters:** value2

- The second '+' operand.
**Returns:** A ValueExp representing the sum or concatenation of
the two arguments. The returned object will be serialized as
an instance of the non-public class

javax.management.BinaryOpValueExp

with an

op

equal to

PLUS

.

- times

```java
public static
ValueExp
times​(
ValueExp
value1,

ValueExp
value2)
```

Returns a binary expression representing the product of two numeric values.

**Parameters:** value1

- The first '*' operand.
**Parameters:** value2

- The second '*' operand.
**Returns:** A ValueExp representing the product. The returned
object will be serialized as an instance of the non-public
class

javax.management.BinaryOpValueExp

with an

op

equal to

TIMES

.

- minus

```java
public static
ValueExp
minus​(
ValueExp
value1,

ValueExp
value2)
```

Returns a binary expression representing the difference between two numeric
values.

**Parameters:** value1

- The first '-' operand.
**Parameters:** value2

- The second '-' operand.
**Returns:** A ValueExp representing the difference between two
arguments. The returned object will be serialized as an
instance of the non-public class

javax.management.BinaryOpValueExp

with an

op

equal to

MINUS

.

- div

```java
public static
ValueExp
div​(
ValueExp
value1,

ValueExp
value2)
```

Returns a binary expression representing the quotient of two numeric
values.

**Parameters:** value1

- The first '/' operand.
**Parameters:** value2

- The second '/' operand.
**Returns:** A ValueExp representing the quotient of two arguments.
The returned object will be serialized as an instance of the
non-public class

javax.management.BinaryOpValueExp

with an

op

equal to

DIV

.

- initialSubString

```java
public static
QueryExp
initialSubString​(
AttributeValueExp
a,

StringValueExp
s)
```

Returns a query expression that represents a matching constraint on
a string argument. The value must start with the given literal string
value.

**Parameters:** a

- An attribute expression.
**Parameters:** s

- A string value expression representing the beginning of the
string value.
**Returns:** The constraint that a matches s. The returned object
will be serialized as an instance of the non-public class

javax.management.MatchQueryExp

.

- anySubString

```java
public static
QueryExp
anySubString​(
AttributeValueExp
a,

StringValueExp
s)
```

Returns a query expression that represents a matching constraint on
a string argument. The value must contain the given literal string
value.

**Parameters:** a

- An attribute expression.
**Parameters:** s

- A string value expression representing the substring.
**Returns:** The constraint that a matches s. The returned object
will be serialized as an instance of the non-public class

javax.management.MatchQueryExp

.

- finalSubString

```java
public static
QueryExp
finalSubString​(
AttributeValueExp
a,

StringValueExp
s)
```

Returns a query expression that represents a matching constraint on
a string argument. The value must end with the given literal string
value.

**Parameters:** a

- An attribute expression.
**Parameters:** s

- A string value expression representing the end of the string
value.
**Returns:** The constraint that a matches s. The returned object
will be serialized as an instance of the non-public class

javax.management.MatchQueryExp

.

- isInstanceOf

```java
public static
QueryExp
isInstanceOf​(
StringValueExp
classNameValue)
```

Returns a query expression that represents an inheritance constraint
on an MBean class.

Example: to find MBeans that are instances of

NotificationBroadcaster

, use

Query.isInstanceOf(Query.value(NotificationBroadcaster.class.getName()))

.

Evaluating this expression for a given

objectName

includes performing

MBeanServer.isInstanceOf(objectName,
((StringValueExp)classNameValue.apply(objectName)).getValue()

.

**Parameters:** classNameValue

- The

StringValueExp

returning the name
of the class of which selected MBeans should be instances.
**Returns:** a query expression that represents an inheritance
constraint on an MBean class. The returned object will be
serialized as an instance of the non-public class

javax.management.InstanceOfQueryExp

.
**Since:** 1.6

---

#### Method Detail

and

```java
public static
QueryExp
and​(
QueryExp
q1,

QueryExp
q2)
```

Returns a query expression that is the conjunction of two other query
expressions.

**Parameters:** q1

- A query expression.
**Parameters:** q2

- Another query expression.
**Returns:** The conjunction of the two arguments. The returned object
will be serialized as an instance of the non-public class

javax.management.AndQueryExp

.

---

#### and

public static

QueryExp

and​(

QueryExp

q1,

QueryExp

q2)

Returns a query expression that is the conjunction of two other query
expressions.

or

```java
public static
QueryExp
or​(
QueryExp
q1,

QueryExp
q2)
```

Returns a query expression that is the disjunction of two other query
expressions.

**Parameters:** q1

- A query expression.
**Parameters:** q2

- Another query expression.
**Returns:** The disjunction of the two arguments. The returned object
will be serialized as an instance of the non-public class

javax.management.OrQueryExp

.

---

#### or

public static

QueryExp

or​(

QueryExp

q1,

QueryExp

q2)

Returns a query expression that is the disjunction of two other query
expressions.

gt

```java
public static
QueryExp
gt​(
ValueExp
v1,

ValueExp
v2)
```

Returns a query expression that represents a "greater than" constraint on
two values.

**Parameters:** v1

- A value expression.
**Parameters:** v2

- Another value expression.
**Returns:** A "greater than" constraint on the arguments. The
returned object will be serialized as an instance of the
non-public class

javax.management.BinaryRelQueryExp

with a

relOp

equal
to

GT

.

---

#### gt

public static

QueryExp

gt​(

ValueExp

v1,

ValueExp

v2)

Returns a query expression that represents a "greater than" constraint on
two values.

geq

```java
public static
QueryExp
geq​(
ValueExp
v1,

ValueExp
v2)
```

Returns a query expression that represents a "greater than or equal
to" constraint on two values.

**Parameters:** v1

- A value expression.
**Parameters:** v2

- Another value expression.
**Returns:** A "greater than or equal to" constraint on the
arguments. The returned object will be serialized as an
instance of the non-public class

javax.management.BinaryRelQueryExp

with a

relOp

equal
to

GE

.

---

#### geq

public static

QueryExp

geq​(

ValueExp

v1,

ValueExp

v2)

Returns a query expression that represents a "greater than or equal
to" constraint on two values.

leq

```java
public static
QueryExp
leq​(
ValueExp
v1,

ValueExp
v2)
```

Returns a query expression that represents a "less than or equal to"
constraint on two values.

**Parameters:** v1

- A value expression.
**Parameters:** v2

- Another value expression.
**Returns:** A "less than or equal to" constraint on the arguments.
The returned object will be serialized as an instance of the
non-public class

javax.management.BinaryRelQueryExp

with a

relOp

equal
to

LE

.

---

#### leq

public static

QueryExp

leq​(

ValueExp

v1,

ValueExp

v2)

Returns a query expression that represents a "less than or equal to"
constraint on two values.

lt

```java
public static
QueryExp
lt​(
ValueExp
v1,

ValueExp
v2)
```

Returns a query expression that represents a "less than" constraint on
two values.

**Parameters:** v1

- A value expression.
**Parameters:** v2

- Another value expression.
**Returns:** A "less than" constraint on the arguments. The
returned object will be serialized as an instance of the
non-public class

javax.management.BinaryRelQueryExp

with a

relOp

equal
to

LT

.

---

#### lt

public static

QueryExp

lt​(

ValueExp

v1,

ValueExp

v2)

Returns a query expression that represents a "less than" constraint on
two values.

eq

```java
public static
QueryExp
eq​(
ValueExp
v1,

ValueExp
v2)
```

Returns a query expression that represents an equality constraint on
two values.

**Parameters:** v1

- A value expression.
**Parameters:** v2

- Another value expression.
**Returns:** A "equal to" constraint on the arguments. The
returned object will be serialized as an instance of the
non-public class

javax.management.BinaryRelQueryExp

with a

relOp

equal
to

EQ

.

---

#### eq

public static

QueryExp

eq​(

ValueExp

v1,

ValueExp

v2)

Returns a query expression that represents an equality constraint on
two values.

between

```java
public static
QueryExp
between​(
ValueExp
v1,

ValueExp
v2,

ValueExp
v3)
```

Returns a query expression that represents the constraint that one
value is between two other values.

**Parameters:** v1

- A value expression that is "between" v2 and v3.
**Parameters:** v2

- Value expression that represents a boundary of the constraint.
**Parameters:** v3

- Value expression that represents a boundary of the constraint.
**Returns:** The constraint that v1 lies between v2 and v3. The
returned object will be serialized as an instance of the
non-public class

javax.management.BetweenQueryExp

.

---

#### between

public static

QueryExp

between​(

ValueExp

v1,

ValueExp

v2,

ValueExp

v3)

Returns a query expression that represents the constraint that one
value is between two other values.

match

```java
public static
QueryExp
match​(
AttributeValueExp
a,

StringValueExp
s)
```

Returns a query expression that represents a matching constraint on
a string argument. The matching syntax is consistent with file globbing:
supports "

?

", "

*

", "

[

",
each of which may be escaped with "

\

";
character classes may use "

!

" for negation and
"

-

" for range.
(

*

for any character sequence,

?

for a single arbitrary character,

[...]

for a character sequence).
For example:

a*b?c

would match a string starting
with the character

a

, followed
by any number of characters, followed by a

b

,
any single character, and a

c

.

**Parameters:** a

- An attribute expression
**Parameters:** s

- A string value expression representing a matching constraint
**Returns:** A query expression that represents the matching
constraint on the string argument. The returned object will
be serialized as an instance of the non-public class

javax.management.MatchQueryExp

.

---

#### match

public static

QueryExp

match​(

AttributeValueExp

a,

StringValueExp

s)

Returns a query expression that represents a matching constraint on
a string argument. The matching syntax is consistent with file globbing:
supports "

?

", "

*

", "

[

",
each of which may be escaped with "

\

";
character classes may use "

!

" for negation and
"

-

" for range.
(

*

for any character sequence,

?

for a single arbitrary character,

[...]

for a character sequence).
For example:

a*b?c

would match a string starting
with the character

a

, followed
by any number of characters, followed by a

b

,
any single character, and a

c

.

attr

```java
public static
AttributeValueExp
attr​(
String
name)
```

Returns a new attribute expression. See

AttributeValueExp

for a detailed description of the semantics of the expression.

Evaluating this expression for a given

objectName

includes performing

MBeanServer.getAttribute(objectName,
name)

.

**Parameters:** name

- The name of the attribute.
**Returns:** An attribute expression for the attribute named

name

.

---

#### attr

public static

AttributeValueExp

attr​(

String

name)

Returns a new attribute expression. See

AttributeValueExp

for a detailed description of the semantics of the expression.

Evaluating this expression for a given

objectName

includes performing

MBeanServer.getAttribute(objectName,
name)

.

Returns a new attribute expression. See

AttributeValueExp

for a detailed description of the semantics of the expression.

Evaluating this expression for a given

objectName

includes performing

MBeanServer.getAttribute(objectName,
name)

.

attr

```java
public static
AttributeValueExp
attr​(
String
className,

String
name)
```

Returns a new qualified attribute expression.

Evaluating this expression for a given

objectName

includes performing

MBeanServer.getObjectInstance(objectName)

and

MBeanServer.getAttribute(objectName,
name)

.

**Parameters:** className

- The name of the class possessing the attribute.
**Parameters:** name

- The name of the attribute.
**Returns:** An attribute expression for the attribute named name.
The returned object will be serialized as an instance of the
non-public class

javax.management.QualifiedAttributeValueExp

.

---

#### attr

public static

AttributeValueExp

attr​(

String

className,

String

name)

Returns a new qualified attribute expression.

Evaluating this expression for a given

objectName

includes performing

MBeanServer.getObjectInstance(objectName)

and

MBeanServer.getAttribute(objectName,
name)

.

Returns a new qualified attribute expression.

Evaluating this expression for a given

objectName

includes performing

MBeanServer.getObjectInstance(objectName)

and

MBeanServer.getAttribute(objectName,
name)

.

classattr

```java
public static
AttributeValueExp
classattr()
```

Returns a new class attribute expression which can be used in any
Query call that expects a ValueExp.

Evaluating this expression for a given

objectName

includes performing

MBeanServer.getObjectInstance(objectName)

.

**Returns:** A class attribute expression. The returned object
will be serialized as an instance of the non-public class

javax.management.ClassAttributeValueExp

.

---

#### classattr

public static

AttributeValueExp

classattr()

Returns a new class attribute expression which can be used in any
Query call that expects a ValueExp.

Evaluating this expression for a given

objectName

includes performing

MBeanServer.getObjectInstance(objectName)

.

Returns a new class attribute expression which can be used in any
Query call that expects a ValueExp.

Evaluating this expression for a given

objectName

includes performing

MBeanServer.getObjectInstance(objectName)

.

not

```java
public static
QueryExp
not​(
QueryExp
queryExp)
```

Returns a constraint that is the negation of its argument.

**Parameters:** queryExp

- The constraint to negate.
**Returns:** A negated constraint. The returned object will be
serialized as an instance of the non-public class

javax.management.NotQueryExp

.

---

#### not

public static

QueryExp

not​(

QueryExp

queryExp)

Returns a constraint that is the negation of its argument.

in

```java
public static
QueryExp
in​(
ValueExp
val,

ValueExp
[] valueList)
```

Returns an expression constraining a value to be one of an explicit list.

**Parameters:** val

- A value to be constrained.
**Parameters:** valueList

- An array of ValueExps.
**Returns:** A QueryExp that represents the constraint. The
returned object will be serialized as an instance of the
non-public class

javax.management.InQueryExp

.

---

#### in

public static

QueryExp

in​(

ValueExp

val,

ValueExp

[] valueList)

Returns an expression constraining a value to be one of an explicit list.

value

```java
public static
StringValueExp
value​(
String
val)
```

Returns a new string expression.

**Parameters:** val

- The string value.
**Returns:** A ValueExp object containing the string argument.

---

#### value

public static

StringValueExp

value​(

String

val)

Returns a new string expression.

value

```java
public static
ValueExp
value​(
Number
val)
```

Returns a numeric value expression that can be used in any Query call
that expects a ValueExp.

**Parameters:** val

- An instance of Number.
**Returns:** A ValueExp object containing the argument. The
returned object will be serialized as an instance of the
non-public class

javax.management.NumericValueExp

.

---

#### value

public static

ValueExp

value​(

Number

val)

Returns a numeric value expression that can be used in any Query call
that expects a ValueExp.

value

```java
public static
ValueExp
value​(int val)
```

Returns a numeric value expression that can be used in any Query call
that expects a ValueExp.

**Parameters:** val

- An int value.
**Returns:** A ValueExp object containing the argument. The
returned object will be serialized as an instance of the
non-public class

javax.management.NumericValueExp

.

---

#### value

public static

ValueExp

value​(int val)

Returns a numeric value expression that can be used in any Query call
that expects a ValueExp.

value

```java
public static
ValueExp
value​(long val)
```

Returns a numeric value expression that can be used in any Query call
that expects a ValueExp.

**Parameters:** val

- A long value.
**Returns:** A ValueExp object containing the argument. The
returned object will be serialized as an instance of the
non-public class

javax.management.NumericValueExp

.

---

#### value

public static

ValueExp

value​(long val)

Returns a numeric value expression that can be used in any Query call
that expects a ValueExp.

value

```java
public static
ValueExp
value​(float val)
```

Returns a numeric value expression that can be used in any Query call
that expects a ValueExp.

**Parameters:** val

- A float value.
**Returns:** A ValueExp object containing the argument. The
returned object will be serialized as an instance of the
non-public class

javax.management.NumericValueExp

.

---

#### value

public static

ValueExp

value​(float val)

Returns a numeric value expression that can be used in any Query call
that expects a ValueExp.

value

```java
public static
ValueExp
value​(double val)
```

Returns a numeric value expression that can be used in any Query call
that expects a ValueExp.

**Parameters:** val

- A double value.
**Returns:** A ValueExp object containing the argument. The
returned object will be serialized as an instance of the
non-public class

javax.management.NumericValueExp

.

---

#### value

public static

ValueExp

value​(double val)

Returns a numeric value expression that can be used in any Query call
that expects a ValueExp.

value

```java
public static
ValueExp
value​(boolean val)
```

Returns a boolean value expression that can be used in any Query call
that expects a ValueExp.

**Parameters:** val

- A boolean value.
**Returns:** A ValueExp object containing the argument. The
returned object will be serialized as an instance of the
non-public class

javax.management.BooleanValueExp

.

---

#### value

public static

ValueExp

value​(boolean val)

Returns a boolean value expression that can be used in any Query call
that expects a ValueExp.

plus

```java
public static
ValueExp
plus​(
ValueExp
value1,

ValueExp
value2)
```

Returns a binary expression representing the sum of two numeric values,
or the concatenation of two string values.

**Parameters:** value1

- The first '+' operand.
**Parameters:** value2

- The second '+' operand.
**Returns:** A ValueExp representing the sum or concatenation of
the two arguments. The returned object will be serialized as
an instance of the non-public class

javax.management.BinaryOpValueExp

with an

op

equal to

PLUS

.

---

#### plus

public static

ValueExp

plus​(

ValueExp

value1,

ValueExp

value2)

Returns a binary expression representing the sum of two numeric values,
or the concatenation of two string values.

times

```java
public static
ValueExp
times​(
ValueExp
value1,

ValueExp
value2)
```

Returns a binary expression representing the product of two numeric values.

**Parameters:** value1

- The first '*' operand.
**Parameters:** value2

- The second '*' operand.
**Returns:** A ValueExp representing the product. The returned
object will be serialized as an instance of the non-public
class

javax.management.BinaryOpValueExp

with an

op

equal to

TIMES

.

---

#### times

public static

ValueExp

times​(

ValueExp

value1,

ValueExp

value2)

Returns a binary expression representing the product of two numeric values.

minus

```java
public static
ValueExp
minus​(
ValueExp
value1,

ValueExp
value2)
```

Returns a binary expression representing the difference between two numeric
values.

**Parameters:** value1

- The first '-' operand.
**Parameters:** value2

- The second '-' operand.
**Returns:** A ValueExp representing the difference between two
arguments. The returned object will be serialized as an
instance of the non-public class

javax.management.BinaryOpValueExp

with an

op

equal to

MINUS

.

---

#### minus

public static

ValueExp

minus​(

ValueExp

value1,

ValueExp

value2)

Returns a binary expression representing the difference between two numeric
values.

div

```java
public static
ValueExp
div​(
ValueExp
value1,

ValueExp
value2)
```

Returns a binary expression representing the quotient of two numeric
values.

**Parameters:** value1

- The first '/' operand.
**Parameters:** value2

- The second '/' operand.
**Returns:** A ValueExp representing the quotient of two arguments.
The returned object will be serialized as an instance of the
non-public class

javax.management.BinaryOpValueExp

with an

op

equal to

DIV

.

---

#### div

public static

ValueExp

div​(

ValueExp

value1,

ValueExp

value2)

Returns a binary expression representing the quotient of two numeric
values.

initialSubString

```java
public static
QueryExp
initialSubString​(
AttributeValueExp
a,

StringValueExp
s)
```

Returns a query expression that represents a matching constraint on
a string argument. The value must start with the given literal string
value.

**Parameters:** a

- An attribute expression.
**Parameters:** s

- A string value expression representing the beginning of the
string value.
**Returns:** The constraint that a matches s. The returned object
will be serialized as an instance of the non-public class

javax.management.MatchQueryExp

.

---

#### initialSubString

public static

QueryExp

initialSubString​(

AttributeValueExp

a,

StringValueExp

s)

Returns a query expression that represents a matching constraint on
a string argument. The value must start with the given literal string
value.

anySubString

```java
public static
QueryExp
anySubString​(
AttributeValueExp
a,

StringValueExp
s)
```

Returns a query expression that represents a matching constraint on
a string argument. The value must contain the given literal string
value.

**Parameters:** a

- An attribute expression.
**Parameters:** s

- A string value expression representing the substring.
**Returns:** The constraint that a matches s. The returned object
will be serialized as an instance of the non-public class

javax.management.MatchQueryExp

.

---

#### anySubString

public static

QueryExp

anySubString​(

AttributeValueExp

a,

StringValueExp

s)

Returns a query expression that represents a matching constraint on
a string argument. The value must contain the given literal string
value.

finalSubString

```java
public static
QueryExp
finalSubString​(
AttributeValueExp
a,

StringValueExp
s)
```

Returns a query expression that represents a matching constraint on
a string argument. The value must end with the given literal string
value.

**Parameters:** a

- An attribute expression.
**Parameters:** s

- A string value expression representing the end of the string
value.
**Returns:** The constraint that a matches s. The returned object
will be serialized as an instance of the non-public class

javax.management.MatchQueryExp

.

---

#### finalSubString

public static

QueryExp

finalSubString​(

AttributeValueExp

a,

StringValueExp

s)

Returns a query expression that represents a matching constraint on
a string argument. The value must end with the given literal string
value.

isInstanceOf

```java
public static
QueryExp
isInstanceOf​(
StringValueExp
classNameValue)
```

Returns a query expression that represents an inheritance constraint
on an MBean class.

Example: to find MBeans that are instances of

NotificationBroadcaster

, use

Query.isInstanceOf(Query.value(NotificationBroadcaster.class.getName()))

.

Evaluating this expression for a given

objectName

includes performing

MBeanServer.isInstanceOf(objectName,
((StringValueExp)classNameValue.apply(objectName)).getValue()

.

**Parameters:** classNameValue

- The

StringValueExp

returning the name
of the class of which selected MBeans should be instances.
**Returns:** a query expression that represents an inheritance
constraint on an MBean class. The returned object will be
serialized as an instance of the non-public class

javax.management.InstanceOfQueryExp

.
**Since:** 1.6

---

#### isInstanceOf

public static

QueryExp

isInstanceOf​(

StringValueExp

classNameValue)

Returns a query expression that represents an inheritance constraint
on an MBean class.

Example: to find MBeans that are instances of

NotificationBroadcaster

, use

Query.isInstanceOf(Query.value(NotificationBroadcaster.class.getName()))

.

Evaluating this expression for a given

objectName

includes performing

MBeanServer.isInstanceOf(objectName,
((StringValueExp)classNameValue.apply(objectName)).getValue()

.

Example: to find MBeans that are instances of

NotificationBroadcaster

, use

Query.isInstanceOf(Query.value(NotificationBroadcaster.class.getName()))

.

Evaluating this expression for a given

objectName

includes performing

MBeanServer.isInstanceOf(objectName,
((StringValueExp)classNameValue.apply(objectName)).getValue()

.

---

