# VUE.JS

## getting started:

Get [Vue.js devtools](https://chrome.google.com/webstore/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd) from chrome and _Allow access to file urls_ in chrome settings.

--------------------------------------------------------------------------------

### Expressions

- _Expressions_ - `{{ variable_name }}`

eg:

_index.html_

```html
<div id="app">
  <h1>{{ product }}</h1>
</div>
```

_main.js_

```javascript
var app new Vue({
  el: '#app'
  data: {
    product: 'ham'

  }
})
```

You can change the var value for testing by opening the console via _inspect_

--------------------------------------------------------------------------------

### Absolute Binding

**v-bind**

_index.html_

```html
<div class="app">
  <img v-bind:src="image">
</div>
```

_main.js_

```javascript
var app new Vue({
  el: '#app'
  data: {
    products: 'ham'
    image: '.assets/the_image.jpg'

  }
})
```

v-bind short hand

:src="image"

instead of:

v-bind:src="image"

--------------------------------------------------------------------------------

### conditional rendering - IF ELSE

_index.html_

```html
<div id="app">
  <div class="product">
    <div class="product-info">
      <p v-if="inStock">In stock</p>
      <p v-else>Out of stock</p>
    </div>
  </div>
</div>
```

_main.js_

```javascript
var app new Vue({
  el: '#app'
  data: {
    product: 'ham'
    inStock: true
  }
})
```

More complex example:

```html
<p v-if="amount > 20">In stock</p>
<p v-else-if="amount <= 20 && amount >0">Low stock</p>
<p v-else>Out of stock</p>
```

and

```javascript
amount: 15
```

**v-show**

```html
<p v-show="inStock">In stock</p>
```

Wont show if v-show in **false**

--------------------------------------------------------------------------------

### list rendering - FOR LOOPS

**v-for**

```html
<div id="app">
  <div class="product">
    <div class="product-info">
      <ul>
        <li v-for="details in details">{{ details }}</li>
      </ul>
      <div v-for "varient in varients" : key=varient.variantId"">
        <p>{{ varient.varienColor }}</p>
    </div>
  </div>
</div>
```

li is like dot points

_main.js_

```javascript
var app new Vue({
  el: '#app'
  data: {
    details: ['Detail1','Detail2','Detail3','Detail4']
    varients: [
      {
        varientId: 123
        varientColor: "blue"
      },
      {
        varientId: 124
        varientColor: "green"
      }

    ]
  }
})
```

--------------------------------------------------------------------------------

### Event Heading

[v-on Docs](https://vuejs.org/v2/guide/events.html)

_index.html_

```html
<div id="app">
  <div class="product">
    <div class="product-info">
      <button v-on:click="cart += 1" >Add to Cart</button>
      <div>
        <p>Items in cart: {{ cart }}</p>
      </div>

    </div>
  </div>
</div>
```

_main.js_

```javascript
var app new Vue({
  el: '#app'
  data: {
    cart: 0
  }
})
```

**The same with a js method**

_index.html_

```html
<div id="app">
  <div class="product">
    <div class="product-info">
      <button v-on:click="addToCart" >Add to Cart</button>
      <div>
        <p>Items in cart: {{ cart }}</p>
      </div>

    </div>
  </div>
</div>
```

_main.js_

```javascript
var app new Vue({
  el: '#app'
  data: {
    cart: 0
    addToCart: function () {
      this.cart += 1
    }
  }
})
```

Shorthand for v-on:

`@`

For more mouse events see [here](https://javascript.info/mouse-events-basics#mouse-event-types)

### Class & style binding
