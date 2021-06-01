<template>
  <div id="content">
    <Notification message="Отправить архив для рендеринга" :is-error="false" :is-visible="true"/>
    <hr/>
    <div id="wrapper">
      <div id="controlContainer">
        <label> Архив c сценой и текстурами:
          <!-- к сожалению v-model не поддерживает input type="file" поэтому "брать" файл из input придётся вручную-->
          <input id="fileInput" type="file" accept=".zip" class="colored illuminated animated rounded">
        </label>
        <br/>
        <label> Ширина:
          <input id="widthInput" value="500" type="number" placeholder="[2 ; 15360]" class="colored illuminated animated rounded">
        </label>
        <br/>
        <label> Высота:
          <input id="heightInput" value="281" type="number" placeholder="[2 ; 15360]" class="colored illuminated animated rounded">
        </label>
        <br/>
        <label> Формат:
          <select id="formatInput" class="colored illuminated animated rounded">
            <option value="JPEG" selected="true">JPEG</option>
            <option value="PNG">PNG</option>
            <option value="BMP">BMP</option>
          </select>
        </label>
        <br/>
        <label> Сжатие:
          <input id="compressionInput" value="0" type="number" placeholder=" min [0 ; 100] max" class="colored illuminated animated rounded">
        </label>
        <br/>
        <label> Сглаживание:
          <select id="aaInput" class="colored illuminated animated rounded">
            <option value="OFF">OFF</option>
            <option value="FXAA" selected="true">FXAA</option>
            <option value="SSAA 5x">SSAA 5x</option>
            <option value="SSAA 8x">SSAA 8x</option>
            <option value="SSAA 11x">SSAA 11x</option>
            <option value="SSAA 16x">SSAA 16x</option>
            <option value="SSAA 32x">SSAA 32x</option>
          </select>
        </label>
        <CheckButton id="submitBtn" color="red" label="Отправить" @click.native="validateForm"/>
      </div>
      <div>
        <img id="imgContainer" src="/assets/img/blender_community_badge.png" class="bordered rounded illuminated animated">
      </div>
    </div>
    <hr/>
    <div id="outputContainer">
      <Notification v-bind="statusLbl"/>
      <table v-if="log.length !== 0" id="outputTable">
        <thead>
        <tr>
          <th>Лог рендеринга</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="line in log" :key="line">
          <td>{{ line }}</td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import CheckButton from "@/components/CheckButton";
import Notification from "@/components/Notification";

export default {
  name: "RenderControl",
  components: {Notification, CheckButton},
  data() {
    return {
      statusLbl: {
        message: "",
        isError: false,
        isVisible: false
      },
      timerId: null,
      isAnimated: false,
      animatedText: Array.of("Ждите —", "Ждите \\", "Ждите |", "Ждите /"),
      log: Array.of()
    }
  },
  methods: {
    validateForm() {
      try {
        const reqForm = new FormData()
        const f = document.getElementById("fileInput").files[0]
        if (f !== undefined && f.name.includes(".zip")) reqForm.append("INPUT_FILE", f)
        else throw TypeError("Разрешены только файлы формата zip")
        const w = document.getElementById("widthInput").value
        const h = document.getElementById("heightInput").value
        if (Array.of(w, h).every( it => (it >= 2 && it <= 15360) )) {
          reqForm.append("WIDTH", w)
          reqForm.append("HEIGHT", h)
        } else throw RangeError("Разрешение по X или Y может быть в интервале [2 ; 15360]")
        const format = document.getElementById("formatInput").value
        reqForm.append("FORMAT", format)
        const compr = document.getElementById("compressionInput").value
        if (compr >= 0 && compr <= 100) reqForm.append("COMPRESSION", compr)
        else throw RangeError("Сжатие в интервале min [0 ; 100] max")
        const aa = document.getElementById("aaInput").value
        reqForm.append("ANTIALIASING_ALGORITHM", aa)
        this.sendForm(reqForm)
      } catch (e) {
        this.statusLbl.isError = true
        this.statusLbl.message = e.message
      }
    },
    sendForm(reqForm) {
      document.getElementById("submitBtn").disabled = true
      this.isAnimated = true
      this.statusLbl.isVisible = true
      this.$axios.post("render", reqForm, {
        headers: {
          "Content-Type": "multipart/form-data"
        }
      }).then( response => {
        this.statusLbl.isError = false
        this.statusLbl.isVisible = false
        this.log = response.data.log
        document.getElementById("imgContainer").src = `data:image/jpeg;base64, ${response.data.img}`
      }).catch( error => {
        this.statusLbl.isError = true
        this.statusLbl.message = error.response.statusText
      }).finally( () => {
        document.getElementById("submitBtn").disabled = true
        this.isAnimated = false
      })
    }
  },
  watch: {
    isAnimated: function(newVal) {
      let counter = 0
      if (newVal === true) {
        this.timerId = setInterval(() => {
          this.statusLbl.message = this.animatedText[counter % this.animatedText.length]
          counter++
        }, 250)
      } else clearTimeout(this.timerId)
    }
  }
}
</script>

<style scoped>
#content {
  margin-left: 5%;
  margin-right: 5%;
}

#wrapper {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

#wrapper * {
  min-width: 50%;
  margin-top: 13px;
  margin-bottom: 13px;
}

#outputContainer { margin-bottom: 130px }

input, img { background-color: white }

img {
  box-shadow: inset 0 0 7px 1px gray;
  max-width: 500px;
  max-height: 281px;
  object-fit: contain;
}

#outputTable {
  border: 1px solid #000720;
  border-collapse: collapse;
  margin: auto;
  width: 90%;
}

#outputTable th {
  background-color: #000720;
  color: white;
}

#outputTable td { text-align: start }

#outputTable * { padding: 15px }
</style>