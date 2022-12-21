/*! gumshoe v4.0.1 | (c) 2019 Chris Ferdinandi | MIT License | http://github.com/cferdinandi/gumshoe */

Element.prototype.closest || (Element.prototype.matches || (Element.prototype.matches = Element.prototype.msMatchesSelector || Element.prototype.webkitMatchesSelector), Element.prototype.closest = function (t) {
    var e = this;
    if (!document.documentElement.contains(this)) return null;
    do {
        if (e.matches(t)) return e;
        e = e.parentElement
    } while (null !== e);
    return null
}), (function () {
    if ("function" == typeof window.CustomEvent) return !1;

    function t(t, e) {
        e = e || {bubbles: !1, cancelable: !1, detail: void 0};
        var n = document.createEvent("CustomEvent");
        return n.initCustomEvent(t, e.bubbles, e.cancelable, e.detail), n
    }

    t.prototype = window.Event.prototype, window.CustomEvent = t
})(), (function (t, e) {
    "function" == typeof define && define.amd ? define([], (function () {
        return e(t)
    })) : "object" == typeof exports ? module.exports = e(t) : t.Gumshoe = e(t)
})("undefined" != typeof global ? global : "undefined" != typeof window ? window : this, (function (t) {
    "use strict";
    var e = {
        navClass: "active",
        contentClass: "active",
        nested: !1,
        nestedClass: "active",
        offset: 0,
        reflow: !1,
        events: !0
    }, n = function (t, e, n) {
        if (n.settings.events) {
            var o = new CustomEvent(t, {bubbles: !0, cancelable: !0, detail: n});
            e.dispatchEvent(o)
        }
    }, o = function (t) {
        var e = 0;
        if (t.offsetParent) for (; t;) e += t.offsetTop, t = t.offsetParent;
        return e >= 0 ? e : 0
    }, s = function (t) {
        t.sort((function (t, e) {
            return o(t.content) < o(e.content) ? -1 : 1
        }))
    }, r = function (t, e) {
        var n = t.getBoundingClientRect(), o = (function (t) {
            return "function" == typeof t.offset ? parseFloat(t.offset()) : parseFloat(t.offset)
        })(e);
        return parseInt(n.top, 10) <= o && parseInt(n.bottom, 10) > o
    }, i = function (t, e) {
        if (e.nested) {
            var n = t.parentNode.closest("li");
            n && (n.classList.remove(e.nestedClass), i(n, e))
        }
    }, c = function (t, e) {
        if (t) {
            var o = t.nav.closest("li");
            o && (o.classList.remove(e.navClass), t.content.classList.remove(e.contentClass), i(o, e), n("gumshoeDeactivate", o, {
                link: t.nav,
                content: t.content,
                settings: e
            }))
        }
    }, a = function (t, e) {
        if (e.nested) {
            var n = t.parentNode.closest("li");
            n && (n.classList.add(e.nestedClass), a(n, e))
        }
    };
    return function (o, i) {
        var l, u, f, d, v, m = {};
        m.setup = function () {
            l = document.querySelectorAll(o), u = [], Array.prototype.forEach.call(l, (function (t) {
                var e = document.getElementById(decodeURIComponent(t.hash.substr(1)));
                e && u.push({nav: t, content: e})
            })), s(u)
        }, m.detect = function () {
            var t = (function (t, e) {
                for (var n = t.length - 1; n >= 0; n--) if (r(t[n].content, e)) return t[n]
            })(u, v);
            t ? f && t.content === f.content || (c(f, v), (function (t, e) {
                if (t) {
                    var o = t.nav.closest("li");
                    o && (o.classList.add(e.navClass), t.content.classList.add(e.contentClass), a(o, e), n("gumshoeActivate", o, {
                        link: t.nav,
                        content: t.content,
                        settings: e
                    }))
                }
            })(t, v), f = t) : f && (c(f, v), f = null)
        };
        var p = function (e) {
            d && t.cancelAnimationFrame(d), d = t.requestAnimationFrame(m.detect)
        }, E = function (e) {
            d && t.cancelAnimationFrame(d), d = t.requestAnimationFrame((function () {
                s(), m.detect()
            }))
        };
        return m.destroy = function () {
            f && c(f), t.removeEventListener("scroll", p, !1), v.reflow && t.removeEventListener("resize", E, !1), u = null, l = null, f = null, d = null, v = null
        }, m.init = function (n) {
            v = (function () {
                var t = {};
                return Array.prototype.forEach.call(arguments, (function (e) {
                    for (var n in e) {
                        if (!e.hasOwnProperty(n)) return;
                        t[n] = e[n]
                    }
                })), t
            })(e, n || {}), m.setup(), m.detect(), t.addEventListener("scroll", p, !1), v.reflow && t.addEventListener("resize", E, !1)
        }, m.init(i), m
    }
}));