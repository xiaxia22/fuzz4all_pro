# Interface XPathFunction

**Source:** `java.xml\javax\xml\xpath\XPathFunction.html`

### Class Description

```java
public interface
XPathFunction
```

XPathFunction

provides access to XPath functions.

Functions are identified by QName and arity in XPath.

**Since:** 1.5

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Object
evaluate​(
List
<?> args)
throws
XPathFunctionException

Evaluate the function with the specified arguments.

To the greatest extent possible, side-effects should be avoided in the
definition of extension functions. The implementation evaluating an
XPath expression is under no obligation to call extension functions in
any particular order or any particular number of times.

**Parameters:**
- args

- The arguments,

null

is a valid value.

**Returns:**
- The result of evaluating the

XPath

function as an

Object

.

**Throws:**
- XPathFunctionException

- If

args

cannot be evaluated with this

XPath

function.

---

### Additional Sections

#### Interface XPathFunction

```java
public interface
XPathFunction
```

XPathFunction

provides access to XPath functions.

Functions are identified by QName and arity in XPath.

**Since:** 1.5

public interface

XPathFunction

XPathFunction

provides access to XPath functions.

Functions are identified by QName and arity in XPath.

XPathFunction

provides access to XPath functions.

Functions are identified by QName and arity in XPath.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Object

evaluate

​(

List

<?> args)

Evaluate the function with the specified arguments.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Object

evaluate

​(

List

<?> args)

Evaluate the function with the specified arguments.

---

#### Method Summary

Evaluate the function with the specified arguments.

============ METHOD DETAIL ==========

- Method Detail

- evaluate

```java
Object
evaluate​(
List
<?> args)
throws
XPathFunctionException
```

Evaluate the function with the specified arguments.

To the greatest extent possible, side-effects should be avoided in the
definition of extension functions. The implementation evaluating an
XPath expression is under no obligation to call extension functions in
any particular order or any particular number of times.

**Parameters:** args

- The arguments,

null

is a valid value.
**Returns:** The result of evaluating the

XPath

function as an

Object

.
**Throws:** XPathFunctionException

- If

args

cannot be evaluated with this

XPath

function.

Method Detail

- evaluate

```java
Object
evaluate​(
List
<?> args)
throws
XPathFunctionException
```

Evaluate the function with the specified arguments.

To the greatest extent possible, side-effects should be avoided in the
definition of extension functions. The implementation evaluating an
XPath expression is under no obligation to call extension functions in
any particular order or any particular number of times.

**Parameters:** args

- The arguments,

null

is a valid value.
**Returns:** The result of evaluating the

XPath

function as an

Object

.
**Throws:** XPathFunctionException

- If

args

cannot be evaluated with this

XPath

function.

---

#### Method Detail

evaluate

```java
Object
evaluate​(
List
<?> args)
throws
XPathFunctionException
```

Evaluate the function with the specified arguments.

To the greatest extent possible, side-effects should be avoided in the
definition of extension functions. The implementation evaluating an
XPath expression is under no obligation to call extension functions in
any particular order or any particular number of times.

**Parameters:** args

- The arguments,

null

is a valid value.
**Returns:** The result of evaluating the

XPath

function as an

Object

.
**Throws:** XPathFunctionException

- If

args

cannot be evaluated with this

XPath

function.

---

#### evaluate

Object

evaluate​(

List

<?> args)
throws

XPathFunctionException

Evaluate the function with the specified arguments.

To the greatest extent possible, side-effects should be avoided in the
definition of extension functions. The implementation evaluating an
XPath expression is under no obligation to call extension functions in
any particular order or any particular number of times.

Evaluate the function with the specified arguments.

To the greatest extent possible, side-effects should be avoided in the
definition of extension functions. The implementation evaluating an
XPath expression is under no obligation to call extension functions in
any particular order or any particular number of times.

---

