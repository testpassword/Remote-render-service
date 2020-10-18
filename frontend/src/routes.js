import Vue from 'vue'
import VueRouter from "vue-router";
import NotFoundError from "@/components/Error";
import RenderControl from "@/components/RenderControl";

Vue.use(VueRouter);

export default new VueRouter({
    mode: "history",
    routes: [
        {
            path: "/",
            name: "main_page",
            component: RenderControl
        },
        {
            path: "/*",
            name: "error_page",
            component: NotFoundError,
            props: {
                default: true,
                errorCode: "404",
                errorMessage: "Страница, которую вы запрашиваете, отсутствует",
                redirectTo: "/"
            }
        }
    ]
});